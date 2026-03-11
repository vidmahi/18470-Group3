# Import necessary libraries and modules
from pymongo import MongoClient

import hardwareDatabase

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
    db = client["HaaS_DB"]
    projects = db["projects"]

    project = projects.find_one({'projectId': projectId})
    return project

# Function to create a new project
def createProject(client, projectName, projectId, description):
    # Create a new project in the database
    db = client["HaaS_DB"]
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
    # Add a user to the specified project
    pass

# Function to update hardware usage in a project
def updateUsage(client, projectId, hwSetName):
    # Update the usage of a hardware set in the specified project
    pass

# Function to check out hardware for a project
def checkOutHW(client, projectId, hwSetName, qty, userId):
    db = client["HaaS_DB"]
    users = db["users"]

    user = users.find_one({"userId": userId, "projects": projectId, 'hwSets': hwSetName})
    
    if user is None:
        return False
    
    space = hardwareDatabase.requestSpace(client, hwSetName, qty)

    if space == True:
        result = users.update_one(
        {"userId": userId},
        {
        "$inc": { "hwSets.$[hwSet].hwSetName": -qty} 
        }
    )
    else:
        return False
    return True
    


# Function to check in hardware for a project
def checkInHW(client, projectId, hwSetName, qty, userId):
    # Check in hardware for the specified project and update availability
    db = client["HaaS_DB"]
    users = db["users"]

    user = users.find_one({"userId": userId, "projects": projectId, 'hwSets': hwSetName})
    
    if user is None:
        return False
    
    space = hardwareDatabase.requestSpace(client, hwSetName, qty)

    if space == True:
        result = users.update_one(
        {"userId": userId},
        {
        "$inc": { "hwSets.$[hwSet].hwSetName": +qty} 
        }
    )
    else:
        return False
    return True

