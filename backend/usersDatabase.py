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
def addUser(client, username, userId, password):
    # Add a new user to the database
    db = client["HaaS_DB"]
    users = db["users"]

    #Check if user already exists
    exist_user = __queryUser(client, username, userId)
    if exist_user is not None:
        return False #The user already exists
    
    #Otherwise, Hash password like def login
    salt = hashlib.sha256(username.encode()).digest()
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100_000
    )

    #Create user document
    user = {
        "username": username, 
        "userId": userId, 
        "password_hash": password_hash, 
        "salt": salt, 
        "projects": []
    }

    users.insert_one(user)
    return True #User has been added!

# Helper function to query a user by username and userId
def __queryUser(client, username, userId):
    # Query and return a user from the database
     db = client["HaaS_DB"]
     users = db["users"]
     return users.find_one({"username": username, "userId": userId}) 

# Function to log in a user
def login(client, username, userId, password):
    # Authenticate a user and return login status
    pass

# Function to add a user to a project
def joinProject(client, userId, projectId):
    # Add a user to a specified project
    pass

# Function to get the list of projects for a user
def getUserProjectsList(client, userId):
    # Get and return the list of projects a user is part of
    pass

