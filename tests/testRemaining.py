import pytest
import hashlib
import os
from app import app
from pymongo import MongoClient


#All Fixtures
@pytest.fixture(scope="module")
def test_client():
    app.config['Testing'] = True
    client = app.test_client()
    yield client

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

@pytest.fixture(autouse=True)
def clean_up(test_db):
    #Before each test, clearing the following
    test_db["hardware"].delete_many({})
    test_db["users"].delete_many({})
    test_db["projects"].delete_many({})



#13.Logging Off
def test_logoff(test_client, test_db):
    test_db["users"].insert_one(
        {"username": "logUser", 
        "userId": "logUser1",
        "password": hash_password("pass"), 
        "projects": []})
    
    response_login = test_client.post('/login', json={"userId": "logUser1", "password": "pass"})
    assert response_login.status_code == 200

    #logging off
    response = test_client.post('/logout', json={"userId": "logUser1"})
    data = response.get_json()
    assert response.status_code == 200
    assert data["success"] is True
    assert data["message"] == "Logged out successfully"

#14. See if state persists if log back in
def test_persist(test_client, test_db):
    test_db["users"].insert_one({
        "username": "loginUser", 
        "userId": "loginUser1", 
        "password": hash_password("pass"),
        "projects": ["proj1"]
    })

    test_db["projects"].insert_one({
        "projectId": "proj1",
        "projectName": "Project1",
        "description": "Test",
        "hwSets": {"HWSet1": 0, "HWSet2":0},
        "users":["loginUser1"]
    })

    #Login
    response_login = test_client.post('/login', json={
        "userId": "loginUser1",
        "password": "pass"
    })
    assert response_login.status_code == 200

    #Check state
    user = test_db["users"].find_one({"userId": "loginUser1"})
    assert "proj1" in user["projects"]


#17. Join Project & Authorization
def test_auth_join(test_client, test_db):
     test_db["users"].insert_one({
        "username": "userB", 
        "userId": "userB", 
        "password": hash_password("pass"),
        "projects": []
    })

     test_db["projects"].insert_one({
        "projectId": "proj1",
        "projectName": "Project1",
        "description": "Test",
        "hwSets": {"HWSet1": 0, "HWSet2":0},
        "users":["loginUser1"]
    })
     
     response = test_client.post('/join_project', json={
         "projectId": "proj1", 
         "userId": "userB"
     })
     data = response.get_json()
     assert response.status_code == 200
     assert "userB" in test_db["projects"].find_one({"projectId": "proj1"})["users"]

#18 - 20. Checkin in HWSet2, increase qty, and checkout
def test_hw2(test_client, test_db):
    test_db["hardware"].insert_one({"name": "HWSet2", "total": 10, "available": 8})
    test_db["users"].insert_one({"username": "user1", "userId": "user1", "password":hash_password("pass"), "projects":["p1"]})
    test_db["projects"].insert_one({"projectId":"p1", "projectName": "p1", "description": "test", "hwSets": {"HWSet1":0, "HWSet2": 2}, "users":["user1"]}) 

    #check-in
    response = test_client.post('/check_in', json={"projectId": "p1", "hwName":"HWSet2", "quantity":1})
    data = response.get_json()
    assert response.status_code == 200
    assert data["success"] is True
    hw = test_db["hardware"].find_one({"name": "HWSet2"})
    assert hw["available"] == 9
    proj = test_db["projects"].find_one({"projectId": "p1"})
    assert proj["hwSets"]["HWSet2"] == 1