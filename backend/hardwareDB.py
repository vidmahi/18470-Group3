# Import necessary libraries and modules
from pymongo import MongoClient

'''
Structure of Hardware Set entry:
HardwareSet = {
    'hwName': hwSetName,
    'capacity': initCapacity,
    'availability': initCapacity
}
'''

# Function to create a new hardware set
def createHardwareSet(client, hwSetName, initCapacity):
    db = client["HaaS_DB"]
    hardware = db["hardware"]
    if hardware.find_one({"hwName": hwSetName}):
        return False
    hwSet = {
        "hwName": hwSetName,
        "capacity": initCapacity,
        "availability": initCapacity
    }
    hardware.insert_one(hwSet)
    return True

# Function to query a hardware set by its name
def queryHardwareSet(client, hwSetName):
    db = client["HaaS_DB"]
    hardware = db["hardware"]
    hw = hardware.find_one({"hwName": hwSetName})
    if hw:
        hw["_id"] = str(hw["_id"])
    return hw

# Function to update the availability of a hardware set
def updateAvailability(client, hwSetName, newAvailability):
    db = client["HaaS_DB"]
    hardware = db["hardware"]
    result = hardware.update_one({"hwName": hwSetName}, {"$set": {"availability": newAvailability}})
    return result.modified_count > 0

# Function to request space from a hardware set
def requestSpace(client, hwSetName, amount):
    db = client["HaaS_DB"]
    hardware = db["hardware"]
    hw = hardware.find_one({"hwName": hwSetName})
    if not hw or hw["availability"] < amount:
        return False
    hardware.update_one({"hwName": hwSetName}, {"$inc": {"availability": -amount}})
    return True

# Function to get all hardware set names
def getAllHwNames(client):
    db = client["HaaS_DB"]
    hardware = db["hardware"]
    hw_names = [hw["hwName"] for hw in hardware.find()]
    return hw_names

