# Import necessary libraries and modules
from bson.objectid import ObjectId
from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
import hashlib
import certifi


# Import custom modules for database interactions
import usersDatabase
import projectsDB
import hardwareDB

# Define the MongoDB connection string
MONGODB_SERVER = "mongodb+srv://test123:test123@cluster0.uy9j5dp.mongodb.net/?appName=Cluster0"
client = MongoClient(MONGODB_SERVER, tlsCAFile=certifi.where())

# Initialize a new Flask web application
app = Flask(__name__)
CORS(app, origins=["http://localhost:5173", "http://127.0.0.1:5173"], supports_credentials=True)

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    userId = data.get("userId")
    password = data.get("password")

    if not userId or not password:
        return jsonify({
            "success": False,
            "message": "Missing userId or password"
        }), 400

    # Use usersDatabase.login
    result = usersDatabase.login(client, userId, password)
    if result is True:
        return jsonify({
            "success": True,
            "message": "Login successful"
        })
    elif result == "incorrect_password":
        return jsonify({
            "success": False,
            "message": "Incorrect password"
        }), 401
    else:
        return jsonify({
            "success": False,
            "message": "User does not exist"
        }), 404

# Route for the main page (Work in progress)
@app.route('/main', methods=['POST'])
def mainPage():
    data = request.get_json()
    userId = data.get("userId")
    if not userId:
        return jsonify({"success": False, "message": "Missing userId"}), 400
    projects = usersDatabase.getUserProjectsList(client, userId)
    return jsonify({"success": True, "projects": projects})

# Route for joining a project
@app.route('/join_project', methods=['POST'])
def join_project():
    data = request.get_json()
    userId = data.get("userId")
    projectId = data.get("projectId")
    if not userId or not projectId:
        return jsonify({"success": False, "message": "Missing userId or projectId"}), 400
    result = usersDatabase.joinProject(client, userId, projectId)
    if result:
        return jsonify({"success": True, "message": "Joined project successfully"})
    else:
        return jsonify({"success": False, "message": "Failed to join project"}), 400

# Route for adding a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    userId = data.get("userId")
    password = data.get("password")

    if not userId or not password:
        return jsonify({
            "success": False,
            "message": "Missing userId or password"
        }), 400

    result = usersDatabase.addUser(client, userId, password)
    if result:
        return jsonify({
            "success": True,
            "message": "User added successfully"
        })
    else:
        return jsonify({
            "success": False,
            "message": "User already exists"
        }), 409

# Route for getting the list of user projects
@app.route('/get_user_projects_list', methods=['POST'])
def get_user_projects_list():
    data = request.get_json()
    userId = data.get("userId")
    if not userId:
        return jsonify({"success": False, "message": "Missing userId"}), 400
    projects = usersDatabase.getUserProjectsList(client, userId)
    return jsonify({"success": True, "projects": projects})

# Route for creating a new project
@app.route('/create_project', methods=['POST'])
def create_project():
    data = request.get_json()
    projectName = data.get("projectName")
    projectId = data.get("projectId")
    description = data.get("description")
    if not projectName or not projectId or not description:
        return jsonify({"success": False, "message": "Missing projectName, projectId, or description"}), 400
    result = projectsDB.createProject(client, projectName, projectId, description)
    if result:
        return jsonify({"success": True, "message": "Project created successfully"})
    else:
        return jsonify({"success": False, "message": "Project already exists or failed to create"}), 409

# Route for getting project information
@app.route('/get_project_info', methods=['POST'])
def get_project_info():
    data = request.get_json()
    projectId = data.get("projectId")
    if not projectId:
        return jsonify({"success": False, "message": "Missing projectId"}), 400
    project = projectsDB.queryProject(client, projectId)
    if project:
        return jsonify({"success": True, "project": project})
    else:
        return jsonify({"success": False, "message": "Project not found"}), 404

# Route for getting all hardware names
@app.route('/get_all_hw_names', methods=['POST'])
def get_all_hw_names():
    hw_names = hardwareDB.getAllHwNames(client)
    return jsonify({"success": True, "hardwareNames": hw_names})

# Route for getting hardware information
@app.route('/get_hw_info', methods=['POST'])
def get_hw_info():
    data = request.get_json()
    hwSetName = data.get("hwSetName")
    if not hwSetName:
        return jsonify({"success": False, "message": "Missing hwSetName"}), 400
    hw_info = hardwareDB.queryHardwareSet(client, hwSetName)
    if hw_info:
        return jsonify({"success": True, "hardware": hw_info})
    else:
        return jsonify({"success": False, "message": "Hardware set not found"}), 404

# Route for checking out hardware
@app.route('/check_out', methods=['POST'])
def check_out():
    data = request.get_json()
    projectId = data.get("projectId")
    hwSetName = data.get("hwSetName")
    qty = data.get("qty")
    userId = data.get("userId")
    if not projectId or not hwSetName or qty is None or not userId:
        return jsonify({"success": False, "message": "Missing projectId, hwSetName, qty, or userId"}), 400
    result = projectsDB.checkOutHW(client, projectId, hwSetName, qty, userId)
    if result:
        return jsonify({"success": True, "message": "Checked out hardware successfully"})
    else:
        return jsonify({"success": False, "message": "Failed to check out hardware"}), 400

# Route for checking in hardware
@app.route('/check_in', methods=['POST'])
def check_in():
    data = request.get_json()
    projectId = data.get("projectId")
    hwSetName = data.get("hwSetName")
    qty = data.get("qty")
    userId = data.get("userId")
    if not projectId or not hwSetName or qty is None or not userId:
        return jsonify({"success": False, "message": "Missing projectId, hwSetName, qty, or userId"}), 400
    result = projectsDB.checkInHW(client, projectId, hwSetName, qty, userId)
    if result:
        return jsonify({"success": True, "message": "Checked in hardware successfully"})
    else:
        return jsonify({"success": False, "message": "Failed to check in hardware"}), 400

# Route for creating a new hardware set
@app.route('/create_hardware_set', methods=['POST'])
def create_hardware_set():
    data = request.get_json()
    hwSetName = data.get("hwSetName")
    initCapacity = data.get("initCapacity")
    if not hwSetName or initCapacity is None:
        return jsonify({"success": False, "message": "Missing hwSetName or initCapacity"}), 400
    result = hardwareDB.createHardwareSet(client, hwSetName, initCapacity)
    if result:
        return jsonify({"success": True, "message": "Hardware set created successfully"})
    else:
        return jsonify({"success": False, "message": "Failed to create hardware set"}), 400

# Route for checking the inventory of projects
@app.route('/api/inventory', methods=['GET'])
def check_inventory():
    db = client["HaaS_DB"]
    projects = db["projects"].find()
    project_list = []
    for project in projects:
        project["_id"] = str(project["_id"])
        project_list.append(project)
    return jsonify({"success": True, "projects": project_list})

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)