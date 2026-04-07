#Will test 7-11 
import pytest
import hashlib
import os
from app import app
from pymongo import MongoClient

#Same Fixtures
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

#NEW FIXTURES
#Fixture for Users/Projects/Hardware
@pytest.fixture
def setup_project_hw(test_db):

    test_db["hardware"].insert_many([
        {"name": "HWSet1", "total": 100, "available":100}, 
        {"name": "HWSet2", "total": 100, "available":100}
    ])

    user = {
        'username': 'user1',
        'userId': 'hwUser1',
        'password': hash_password('hwPass'),
        'projects': []
    }
    test_db["users"].insert_one(user)

    project = {
        'projectName': 'Test Project',
        'projectId': 'p101', 
        'description': "Project for test cases",
        'hwSets': {"HWSet1": 0, "HWSet2":0},
        'users': ['hwUser1'], 
    }
    test_db["projects"].insert_one(project)

    return True

#7. Checking out Hardware Set 1
def test_checkout_hw1(test_client, test_db, setup_project_hw):

    hw_current = test_db["hardware"].find_one({'name': 'HWSet1'})['available']
    project_current = test_db["projects"].find_one({'projectId': 'p101'})['hwSets']['HWSet1']

    response = test_client.post('/check_out', json={
        'projectId': 'p101', 
        'hwName': 'HWSet1', 
        'quantity': 1
    })
    data = response.get_json()
    assert response.status_code == 200
    assert data["success"] is True
    assert data["message"] == "Hardware checked out successfully"

    #9. See if available quantities are reduced in DB
    hw_remaining = test_db["hardware"].find_one({'name': 'HWSet1'})['available']
    assert hw_remaining == hw_current - 1

    project_new = test_db["projects"].find_one({'projectId': 'p101'})['hwSets']['HWSet1']
    assert project_new == project_current + 1


#8. Checking out Hardware Set 2
def test_checkout_hw2(test_client, test_db, setup_project_hw):
        hw_current = test_db["hardware"].find_one({'name': 'HWSet2'})['available']
        project_current = test_db["projects"].find_one({'projectId': 'p101'})['hwSets']['HWSet2']

        response = test_client.post('/check_out', json={
            'projectId': 'p101', 
            'hwName': 'HWSet2', 
            'quantity': 2
        })
        data = response.get_json()
        assert response.status_code == 200
        assert data["success"] is True
        assert data["message"] == "Hardware checked out successfully"

        #9. See if available quantities are reduced in DB
        hw_remaining = test_db["hardware"].find_one({'name': 'HWSet2'})['available']
        assert hw_remaining == hw_current - 2

        project_new = test_db["projects"].find_one({'projectId': 'p101'})['hwSets']['HWSet2']
        assert project_new == project_current + 2 


#10. Trying to checkout more than avail.
def test_checkout_fail(test_client, test_db, setup_project_hw):
     hw_current = test_db["hardware"].find_one({'name': 'HWSet1'})['available']

     response = test_client.post('/check_out', json={
          'projectId': 'p101', 
          'hwName': 'HWSet1', 
          'quantity': hw_current + 1
     })

     data = response.get_json()
     assert response.status_code in [400,409]
     assert data["success"] is False       

#11. Checking IN Hardware Set 1 unit
def test_checkin_hw1(test_client, test_db, setup_project_hw):
     #Check something out, and then return it
     test_client.post('/check_out', json={
          'projectId': 'p101', 
          'hwName': 'HWSet1', 
          'quantity': 1
     })

     hw_current = test_db["hardware"].find_one({'name': 'HWSet1'})['available']
     proj_current = test_db["projects"].find_one({'projectId': 'p101'})["hwSets"]["HWSet1"]

     response = test_client.post('/check_in', json ={
          'projectId': 'p101', 
          'hwName': 'HWSet1', 
          'quantity': 1
     })

     data = response.get_json()

     assert response.status_code == 200
     assert data["success"] is True
     assert data["message"] == "Hardware checked in successfully"

     hw_new = test_db["hardware"].find_one({'name': 'HWSet1'})['available']
     assert hw_new == hw_current + 1

     proj_new = test_db["projects"].find_one({'projectId': 'p101'})["hwSets"]["HWSet1"]
     assert proj_new == proj_current - 1

     
