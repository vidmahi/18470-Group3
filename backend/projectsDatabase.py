# Import necessary libraries and modules
from pymongo import MongoClient

import hardwareDB

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
    pass

# Function to create a new project
def createProject(client, projectName, projectId, description):
    # Create a new project in the database
    pass

# Function to add a user to a project
def addUser(client, projectId, userId):
    db = client["HaaS_DB"]
    projects = db["projects"]

    project = projects.find_one({"projectId": projectId})
    if project is None:
        return False

    result = projects.update_one(
        {"projectId": projectId},
        {"$addToSet": {"users": userId}}
    )

    return result.modified_count > 0

# Function to update hardware usage in a project
def updateUsage(client, projectId, hwSetName):
    db = client["HaaS_DB"]
    projects = db["projects"]

    project = projects.find_one({"projectId": projectId})
    if project is None:
        return False

    if hwSetName not in project["hwSets"]:
        return False

    result = projects.update_one(
        {"projectId": projectId},
        {"$inc": {f"hwSets.{hwSetName}": 1}}
    )

    return result.modified_count > 0

# Function to check out hardware for a project
def checkOutHW(client, projectId, hwSetName, qty, userId):
    # Check out hardware for the specified project and update availability
    pass

# Function to check in hardware for a project
def checkInHW(client, projectId, hwSetName, qty, userId):
    # Check in hardware for the specified project and update availability
    pass