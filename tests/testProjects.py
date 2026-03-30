import pytest
import hashlib
import os
from app import app
from pymongo import MongoClient

#*Note: Just make sure the routes in app.py return same messages that I asserted. 
#Some methods I didn't see complete, so I just created some messages that should match in app.py when implemented

#Using same fixtures as before
@pytest.fixture(scope="module")
def test_client():
    app.config['Testing'] = True
    client = app.test_client()
    yield client

#Database Fixture
@pytest.fixture(scope="module")
def test_db():
    username = os.getenv('MONGODB_USER')
    password = os.getenv('MONGODB_PASS')

    uri = os.getenv('MONGODB_URI').replace('<db_username>', username).replace('<db_password>', password)

    client = MongoClient(uri)
    test_db = "ECE461L_test" #Just using a seperate db for now
    db = client[test_db]
    yield db
    client.drop_database(test_db)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#4. Test - Create a new project
def test_new_project(test_client, test_db):
    #Creating user first
    test_db["users"].insert_one({
        "username": "projUser",
        "userId": "projUser1", 
        "password": hash_password("projPass"),
        "projects": []
    })

    response = test_client.post('/create_project', json={
        "projectId": "project123", 
        "userId": "projUser1"
    })
    data = response.get_json()
    assert response.status_code == 200
    assert data["success"] is True
    assert data["message"] == "Project created successfully"

    #Also checking DB
    project = test_db["projects"].find_one({"projectId": "project123"})
    assert project is not None
    assert "projUser1" in project["users"]

#5. Try to create a project with existing ID
def test_create_project(test_client, test_db):
    response = test_client.post('/create_project', json={
        "projectId": "project123", 
        "userId": "projUser1"
    })
    data = response.get_json()
    assert response.status_code == 409
    assert data["success"] is False
    assert data["message"] == "Project already exists"

#6. Try joining an existing project
def test_join(test_client, test_db):
    #Add another user to db
    test_db["users"].insert_one({
        "username": "someUser",
        "userId": "someUser1", 
        "password": hash_password("somePass"),
        "projects": []
    })

    response = test_client.post('/join_project', json={
        "projectId": "project123",  #same
        "userId": "someUser1" #diff user
    })
    data = response.get_json()
    assert response.status_code == 200
    assert data["success"] is True
    assert data["message"] == "User added to project successfully"

    #check db too
    project = test_db["projects"].find_one({"projectId": "project123"})
    assert "someUser1" in project["users"]

    user = test_db["users"].find_one({"userId": "someUser1"})
    assert "project123" in user["projects"]