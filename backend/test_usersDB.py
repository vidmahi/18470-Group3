#This is the test file to test functions in usersDatabase.py
from pymongo import MongoClient
import usersDatabase
import projectsDatabase

uri = "mongodb+srv://angelaa_r3:Soccerplayer1_@demo-one.onj3oop.mongodb.net/"
client = MongoClient(uri)

#Test addUser function
userAdded = usersDatabase.addUser(client, "testuser", "1234", "password")
print("User Added:", userAdded)

#Test __queryUser function
user = usersDatabase.__queryUser(client, "testuser", "1234")
print("Queried User:", user)
