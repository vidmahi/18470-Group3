# Import necessary libraries and modules
from pymongo import MongoClient
import hardwareDatabase as hardwareDB
from dotenv import load_dotenv
import os

# Get values from config
config = load_dotenv('config.env')
hardware_db_name = os.getenv('HARDWARE_DB_NAME')

'''
Structure of Project entry:
Project = {
    'projectName': projectName,
    'projectId': projectId,
    'description': description,
    'hwSets': {HW1: 0, HW2: 10, ...},
    'users': [user1, user2, ...]
}
'''

# Function to query a project by its ID
def queryProject(client, projectId):
    # Query and return a project from the database
    db = client[hardware_db_name]
    projects = db["projects"]

    project = projects.find_one({'projectId': projectId})
    return project

# Function to create a new project
def createProject(client, projectName, projectId, description):
    # Create a new project in the database
    db = client[hardware_db_name]
    projects = db["projects"]

    existing_project = projects.find_one({'projectId': projectId})
    
    if existing_project is not None:
        return False
    
    project = {
        "projectName": projectName, 
        "projectId": projectId, 
        "description": description, 
        "hwSets": {}, 
        "users": []
    }

    projects.insert_one(project)
    return True

# Function to add a user to a project
def addUser(client, projectId, userId):
    db = client[hardware_db_name]
    projects = db["projects"]

    project = projects.find_one({"projectID": projectId})

    if project is None:
        return False

    result = projects.update_one(
        {"projectId": projectId},
        {"$addToSet": {"users": userId}}  # prevents duplicates
    )

    return result.modified_count > 0

# Function to update hardware usage in a project
def updateUsage(client, projectId, hwSetName):
    # Update the usage of a hardware set in the specified project
    db = client[hardware_db_name]
    projects = db["projects"]

    project = projects.find_one({"projectID": projectId})

    if project is None:
        return False

    result = projects.update_one(
        {"projectID": projectId},
        {
        "$inc": {"hwSets."+hwSetName: 0} 
        }
    )

    return result.modified_count > 0


# Function to check out hardware for a project
def checkOutHW(client, projectId, hwSetName, qty, userId):
    db = client[hardware_db_name]
    projects = db["projects"]

    project = projects.find_one({"userId": userId, "projectID": projectId})
    
    if project is None:
        return False
    
    space = hardwareDB.requestSpace(client, hwSetName, qty)

    if space == True:
        result = projects.update_one(
        {"projectID": projectId},
        {
        "$inc": {"hwSets."+hwSetName: +qty} 
        }
        )
        return True
    else:
        return False
    
    


# Function to check in hardware for a project
def checkInHW(client, projectId, hwSetName, qty, userId):
    # Check in hardware for the specified project and update availability
    db = client[hardware_db_name]
    projects = db["projects"]

    project = projects.find_one({"userId": userId, "projectID": projectId})
    
    if project is None:
        return False
    
    try:
        hw_qty = project['hwSets'][hwSetName]
    except:
        return False
    
    if(hw_qty < qty):
        return False

    space = hardwareDB.requestSpace(client, hwSetName, -qty)

    if space == True:
        result = projects.update_one(
        {"projectID": projectId},
        {
        "$inc": {"hwSets."+hwSetName: -qty}
        }   
    )
        return True
    else:
        return False
    

