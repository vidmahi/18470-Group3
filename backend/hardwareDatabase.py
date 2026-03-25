# Import necessary libraries and modules
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Get values from config
config = load_dotenv('config.env')
hardware_db_name = os.getenv('HARDWARE_DB_NAME')

'''
Structure of Hardware Set entry:
HardwareSet = {
    'hwName': hwSetName,
    'capacity': initCapacity,
    'availability': initCapacity
}
'''

# Function to create a new hardware set
def createHardwareSet(client : MongoClient, hwSetName : str, initCapacity : int):
    # Create a new hardware set in the database
    result = client[hardware_db_name]["hardware_availability"].insert_one({
        'hwName': hwSetName,
        'capacity': initCapacity,
        'availability': initCapacity
    })
    
    return result

# Function to query a hardware set by its name
def queryHardwareSet(client : MongoClient, hwSetName : str):
    # Query and return a hardware set from the database
    doc = client[hardware_db_name]["hardware_availability"].find_one({"hwName": hwSetName})
    return doc

# Function to request space from a hardware set
def requestSpace(client : MongoClient, hwSetName : str, amount : int):
    # Request a certain amount of hardware and update availability
    # Returns True on Success and False on Failure
    
    # Query Predicates Link: https://www.mongodb.com/docs/manual/reference/mql/query-predicates/
    # Update Operators: https://www.mongodb.com/docs/manual/reference/mql/update/
    project  = client[hardware_db_name]["hardware_availability"].find_one({'hwName': hwSetName})
    availability = project.get("availability")
    if availability < amount and amount > 0:
        return False
    
    doc_result = client[hardware_db_name]["hardware_availability"].find_one_and_update(
        {'hwName': hwSetName},
        {'$inc': {"availability": -amount}},
        return_document=True
    )
    
    return doc_result

# Function to get all hardware set names
def getAllHwNames(client : MongoClient):
    # Get and return a list of all hardware set names
    result = client[hardware_db_name]["hardware_availability"].distinct('hwName')
    return result

if __name__ == "__main__":
    
    # Setup credentials
    username = os.getenv('MONGODB_USER')
    password = os.getenv('MONGODB_PASS')
    
    uri = os.getenv('MONGODB_URI').replace('<db_username>', username).replace('<db_password>', password)
    client = MongoClient(uri)
    
    # Function for testing
    def iterate_db():
        cursor = client[hardware_db_name]["hardware_availability"].find({})
        for doc in cursor:
            print(doc)
            
    print("[INFO] Clearing Hardware Database")
    client.get_database(hardware_db_name).drop_collection("hardware_availability")
    
    print("[INFO] Adding Hardware to the Database")
    createHardwareSet(client, "ARM Graviton", 34)
    createHardwareSet(client, 'AMD Genoa', 12)
    createHardwareSet(client, 'Intel Xeon', 5)
    
    print("[INFO] Querying the ARM Graviton")
    result = queryHardwareSet(client, 'ARM Graviton')
    print(result)
    
    print("[INFO] Printing Hardware Collection Names")
    print(getAllHwNames(client))
    
    print("[INFO] Iterating through the Hardware Database")
    iterate_db()
    
    print("[INFO] Attempt to check out 20 of each device]")
    for hwName in getAllHwNames(client):
        result = requestSpace(client, hwName, 20)
        print(hwName, "Success" if result else "Fail")
        
    print("[INFO] Iterating through the Hardware Database after Checkout")
    iterate_db()
    
    print("[INFO] Testing with multiple threads for race conditions")
    client.get_database(hardware_db_name).drop_collection("hardware_availability")
    createHardwareSet(client, "Testing_Concurrency", 1000)
    from concurrent.futures import ThreadPoolExecutor
    
    def worker():
        devices_requested = 0
        for i in range(1, 21, 1): # 20, 0, -1
            if requestSpace(client, "Testing_Concurrency", i):
                devices_requested += i
        return devices_requested
    
    max_workers = 8
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(worker) for n in range(max_workers)]
        results = [f.result() for f in futures]
    print(f"[INFO] Checked out {sum(results)} devices with threadpool executor.")
    print(f"[INFO] Iterating through DB for verification")
    iterate_db()
    