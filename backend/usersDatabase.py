# Import necessary libraries and modules
from pymongo import MongoClient

import projectsDB

'''
Structure of User entry:
User = {
    'username': username,
    'userId': userId,
    'password': password,
    'projects': [project1_ID, project2_ID, ...]
}
'''

# Function to add a new user
def addUser(client, userId, password):
    db = client["HaaS_DB"]
    users = db["users"]

    # Check if user already exists
    exist_user = __queryUser(client, userId)
    if exist_user is not None:
        return False # The user already exists

    # Use userId as salt source for simplicity
    import hashlib
    salt = hashlib.sha256(userId.encode()).digest()
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100_000
    )

    # Create user document
    user = {
        "userId": userId,
        "password_hash": password_hash,
        "salt": salt,
        "projects": []
    }

    users.insert_one(user)
    return True # User has been added!

# Helper function to query a user by userId
def __queryUser(client, userId):
    db = client["HaaS_DB"]
    users = db["users"]
    return users.find_one({"userId": userId})

# Function to log in a user
import hashlib
def login(client, userId, password):
    db = client["HaaS_DB"]
    users = db["users"]
    user = users.find_one({"userId": userId})
    if user is None:
        return False
    salt = user.get("salt")
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100_000
    )
    if password_hash == user.get("password_hash"):
        return True
    else:
        return "incorrect_password"

# Function to add a user to a project
def joinProject(client, userId, projectId):
    db = client["HaaS_DB"]
    users = db["users"]
    projects = db["projects"]
    user = users.find_one({"userId": userId})
    project = projects.find_one({"projectId": projectId})
    if user is None or project is None:
        return False
    # Add project to user's list if not already present
    if projectId not in user.get("projects", []):
        users.update_one({"userId": userId}, {"$push": {"projects": projectId}})
    # Add user to project's user list if not already present
    if userId not in project.get("users", []):
        projects.update_one({"projectId": projectId}, {"$push": {"users": userId}})
    return True

# Function to get the list of projects for a user
def getUserProjectsList(client, userId):
    db = client["HaaS_DB"]
    users = db["users"]
    projects = db["projects"]
    user = users.find_one({"userId": userId})
    if user is None:
        return []
    project_ids = user.get("projects", [])
    project_list = []
    for pid in project_ids:
        project = projects.find_one({"projectId": pid})
        if project:
            project["_id"] = str(project["_id"])
            project_list.append(project)
    return project_list

