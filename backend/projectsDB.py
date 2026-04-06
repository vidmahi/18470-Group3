# # Import necessary libraries and modules
# from pymongo import MongoClient

# import hardwareDB

# '''
# Structure of Project entry:
# Project = {
#     'projectName': projectName,
#     'projectId': projectId,
#     'description': description,
#     'hwSets': {HW1: 0, HW2: 10, ...},
#     'users': [user1, user2, ...]
# }
# '''

# # Function to query a project by its ID
# def queryProject(client, projectId):
#     db = client["HaaS_DB"]
#     projects = db["projects"]
#     project = projects.find_one({"projectId": projectId})
#     if project:
#         project["_id"] = str(project["_id"])
#     return project

# # Function to create a new project
# def createProject(client, projectName, projectId, description):
#     db = client["HaaS_DB"]
#     projects = db["projects"]
#     if projects.find_one({"projectId": projectId}):
#         return False
#     project = {
#         "projectName": projectName,
#         "projectId": projectId,
#         "description": description,
#         "hwSets": {},
#         "users": []
#     }
#     projects.insert_one(project)
#     return True

# # Function to add a user to a project
# def addUser(client, projectId, userId):
#     db = client["HaaS_DB"]
#     projects = db["projects"]
#     project = projects.find_one({"projectId": projectId})
#     if not project:
#         return False
#     if userId not in project.get("users", []):
#         projects.update_one({"projectId": projectId}, {"$push": {"users": userId}})
#     return True

# # Function to update hardware usage in a project
# def updateUsage(client, projectId, hwSetName):
#     db = client["HaaS_DB"]
#     projects = db["projects"]
#     project = projects.find_one({"projectId": projectId})
#     if not project:
#         return False
#     hwSets = project.get("hwSets", {})
#     if hwSetName not in hwSets:
#         hwSets[hwSetName] = 0
#         projects.update_one({"projectId": projectId}, {"$set": {"hwSets": hwSets}})
#     return True

# # Function to check out hardware for a project
# def checkOutHW(client, projectId, hwSetName, qty, userId):
#     db = client["HaaS_DB"]
#     projects = db["projects"]
#     hardware = db["hardware"]
#     project = projects.find_one({"projectId": projectId})
#     hw = hardware.find_one({"hwName": hwSetName})
#     if not project or not hw:
#         return False
#     if hw["availability"] < qty:
#         return False
#     # Update hardware availability
#     hardware.update_one({"hwName": hwSetName}, {"$inc": {"availability": -qty}})
#     # Update project hardware usage
#     hwSets = project.get("hwSets", {})
#     hwSets[hwSetName] = hwSets.get(hwSetName, 0) + qty
#     projects.update_one({"projectId": projectId}, {"$set": {"hwSets": hwSets}})
#     # Add user to project if not already
#     if userId not in project.get("users", []):
#         projects.update_one({"projectId": projectId}, {"$push": {"users": userId}})
#     return True

# # Function to check in hardware for a project
# def checkInHW(client, projectId, hwSetName, qty, userId):
#     db = client["HaaS_DB"]
#     projects = db["projects"]
#     hardware = db["hardware"]
#     project = projects.find_one({"projectId": projectId})
#     hw = hardware.find_one({"hwName": hwSetName})
#     if not project or not hw:
#         return False
#     hwSets = project.get("hwSets", {})
#     if hwSetName not in hwSets or hwSets[hwSetName] < qty:
#         return False
#     # Update hardware availability
#     hardware.update_one({"hwName": hwSetName}, {"$inc": {"availability": qty}})
#     # Update project hardware usage
#     hwSets[hwSetName] -= qty
#     projects.update_one({"projectId": projectId}, {"$set": {"hwSets": hwSets}})
#     return True

from pymongo import MongoClient
import hardwareDB

"""
Structure of Project entry:
Project = {
    'projectName': projectName,
    'projectId': projectId,
    'description': description,
    'hwSets': {HW1: 0, HW2: 10, ...},
    'users': [user1, user2, ...]
}
"""


def queryProject(client, projectId):
    db = client["HaaS_DB"]
    projects = db["projects"]
    project = projects.find_one({"projectId": projectId})
    if project:
        project["_id"] = str(project["_id"])
    return project


def projectExists(client, projectId):
    db = client["HaaS_DB"]
    projects = db["projects"]
    return projects.find_one({"projectId": projectId}) is not None


def createProject(client, projectName, projectId, description):
    db = client["HaaS_DB"]
    projects = db["projects"]

    if projects.find_one({"projectId": projectId}):
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


def addUser(client, projectId, userId):
    db = client["HaaS_DB"]
    projects = db["projects"]

    project = projects.find_one({"projectId": projectId})
    if not project:
        return False

    if userId not in project.get("users", []):
        projects.update_one(
            {"projectId": projectId},
            {"$addToSet": {"users": userId}}
        )

    return True


def updateUsage(client, projectId, hwSetName):
    db = client["HaaS_DB"]
    projects = db["projects"]

    project = projects.find_one({"projectId": projectId})
    if not project:
        return False

    hwSets = project.get("hwSets", {})
    if hwSetName not in hwSets:
        hwSets[hwSetName] = 0
        projects.update_one({"projectId": projectId}, {"$set": {"hwSets": hwSets}})

    return True


def checkOutHW(client, projectId, hwSetName, qty, userId):
    db = client["HaaS_DB"]
    projects = db["projects"]
    hardware = db["hardware"]

    project = projects.find_one({"projectId": projectId})
    hw = hardware.find_one({"hwName": hwSetName})

    if not project:
        return False, "Project does not exist"

    if not hw:
        return False, "Hardware set does not exist"

    if qty < 1:
        return False, "Quantity must be at least 1"

    available = hw.get("availability", 0)
    if available < qty:
        return False, f"Only {available} unit(s) available"

    hardware.update_one(
        {"hwName": hwSetName},
        {"$inc": {"availability": -qty}}
    )

    hwSets = project.get("hwSets", {})
    hwSets[hwSetName] = hwSets.get(hwSetName, 0) + qty

    projects.update_one(
        {"projectId": projectId},
        {
            "$set": {"hwSets": hwSets},
            "$addToSet": {"users": userId}
        }
    )

    return True, f"Checked out {qty} unit(s) of {hwSetName}"


def checkInHW(client, projectId, hwSetName, qty, userId):
    db = client["HaaS_DB"]
    projects = db["projects"]
    hardware = db["hardware"]

    project = projects.find_one({"projectId": projectId})
    hw = hardware.find_one({"hwName": hwSetName})

    if not project:
        return False, "Project does not exist"

    if not hw:
        return False, "Hardware set does not exist"

    if qty < 1:
        return False, "Quantity must be at least 1"

    hwSets = project.get("hwSets", {})
    current_out = hwSets.get(hwSetName, 0)

    if current_out < qty:
        return False, f"Only {current_out} unit(s) of {hwSetName} are checked out by this project"

    capacity = hw.get("capacity", 0)
    availability = hw.get("availability", 0)
    new_availability = min(capacity, availability + qty)

    hardware.update_one(
        {"hwName": hwSetName},
        {"$set": {"availability": new_availability}}
    )

    hwSets[hwSetName] = current_out - qty

    projects.update_one(
        {"projectId": projectId},
        {"$set": {"hwSets": hwSets}}
    )

    return True, f"Checked in {qty} unit(s) of {hwSetName}"