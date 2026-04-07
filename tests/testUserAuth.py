#User Authentication Test Cases
import pytest
import hashlib
import os
from app import app
from pymongo import MongoClient

#Set Up Environment
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


#1.Check Sign up as new user
def test_signUp(test_client, test_db):
    response = test_client.post('/add_user', json={
        "username": "TestUser1",
        "userId": "testuser1", 
        "password": "pass123"

    })
    data = response.get_json()
    assert response.status_code == 200
    assert data["success"] is True
    assert data["message"] == "User added successfully"

    #Also checking in DB
    user = test_db['users'].find_one({"userId": "testuser1"})
    assert user is not None
    assert user['username'] == "TestUser1"
    assert user['password'] == hash_password("pass123")



#2. Check Signing in with ID/Password
def test_login(test_client, test_db):
    test_db["users"].insert_one({
        "username": "loginUser",
        "userId": "someUser", 
        "password": hash_password("somePass"),
        "projects": []
    })

    response = test_client.post('/login', json={
        "userId": "someUser", 
        "password": "somePass"
    })

    data = response.get_json()
    assert response.status_code == 200
    assert data["success"] is True
    assert data["message"] == "Login successful"


#3. Check Signing in with WRONG ID/Password
def test_login_fail(test_client, test_db):
    test_db["users"].insert_one({
        "username": "wrongUser",
        "userId": "wrongUser", 
        "password": hash_password("correctPass"),
        "projects": []
    })

    response = test_client.post('/login', json={ #Tests wrong password, correct ID
        "userId": "someWrongUser", 
        "password": "wrongPass"
    })

    data = response.get_json()
    assert response.status_code == 401
    assert data["success"] is False
    assert data["message"] == "Incorrect password"

#3. Now, checking with wrong user/not found
def test_user_fail(test_client, test_db):
    response = test_client.post('/login', json={
        "userId": "notFound", 
        "password": "somePass"
    })
    data = response.get_json()
    assert response.status_code == 404
    assert data["success"] is False
    assert data["message"] == "User does not exist"

#15.TA creates new ID and Login
def test_TA(test_client, test_db):
    #Add TA as user
    response = test_client.post('/add_user', json={
        "username": "TAUser",
        "userId": "TAuser", 
        "password": "tapass123"
    })

    data = response.get_json()
    assert response.status_code == 200
    assert data["success"] is True

    #login
    response_login = test_client.post('/login', json={
        "userId": "TAuser", 
        "password": "tapass123"
    })

    data_login = response_login.get_json()
    assert response_login.status_code == 200
    assert data_login["success"] is True
    assert data_login["message"] == "Login successful"