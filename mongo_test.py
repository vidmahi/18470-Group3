from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pprint import pprint
uri = "mongodb+srv://jabirubaydullah_db_user:Wftc77265BpVE0ht@ece461l.4jygotz.mongodb.net/?appName=ECE461L"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    
    database = client.get_database("project_database")
    projects = database.get_collection("project_collection")

    sample_project = {
        'Name': 'Project 1',
        'Description': 'First project',
        'ProjectID': 'A1'
    }

    result = projects.insert_one(sample_project)

    query = { "Name": "Project 1" }

    project = projects.find_one(query)

    pprint(project)

    client.close()

except Exception as e:
    print(e)