# Imports
from pymongo import MongoClient
import hashlib
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
    pass

# Helper function to query a user by username and userId
def __queryUser(client, username, userId):
    # Query and return a user from the database
    pass

# Function to log in a user
def login(client, username, userId, password):
    """
    Authenticate a user using username, userId, and password.
    Returns True if login is successful, False otherwise.
    """
    db = client["HaaS_DB"]
    users = db["users"]

    # Find the user in the database
    user = users.find_one({"username": username, "userId": userId})

    if user is None:
        return False  # User does not exist

    # Re-hash the entered password using the stored salt
    # the 100000 is how many times hashed
    entered_password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        user["salt"],
        100_000
    )

    # Compare hashes
    if entered_password_hash == user["password_hash"]:
        return True
    else:
        return False


def joinProject(client, userId, projectId):
    """
    Add a project ID to a user's project list.
    """
    db = client["HaaS_DB"]
    users = db["users"]

    # Check that project exists
    if not projectsDB.projectExists(client, projectId):
        return False

    # add projct to user's list if not already there
    result = users.update_one(
        {"userId": userId},
        {"$addToSet": {"projects": projectId}}  # prevents duplicates
    )

    return result.modified_count > 0

def getUserProjectsList(client, userId):
    """
    Return the list of project IDs for a given user.
    """
    db = client["HaaS_DB"]
    users = db["users"]

    user = users.find_one({"userId": userId})

    if user is None:
        return []

    return user.get("projects", [])