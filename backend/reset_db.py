from pymongo import MongoClient
from dotenv import load_dotenv
import projectsDatabase as projectsDB
import hashlib
import os

# Get values from config
config = load_dotenv('config.env')
hardware_db_name = os.getenv('HARDWARE_DB_NAME')

# Setup credentials
username = os.getenv('MONGODB_USER')
password = os.getenv('MONGODB_PASS')

uri = os.getenv('MONGODB_URI').replace('<db_username>', username).replace('<db_password>', password)
client = MongoClient(uri)
db = client[hardware_db_name]

for collection_name in ["hardware_availability", "users", "projects"]:
    if collection_name in db.list_collection_names():
        db.drop_collection(collection_name)
    db.create_collection(collection_name)

client.close()