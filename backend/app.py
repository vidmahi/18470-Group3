# # # # Import necessary libraries and modules
# # # from bson.objectid import ObjectId
# # # from flask import Flask, request, jsonify
# # # from pymongo import MongoClient
# # # from flask_cors import CORS
# # # import hashlib
# # # import certifi


# # # # Import custom modules for database interactions
# # # import usersDatabase
# # # import projectsDB
# # # import hardwareDB

# # # # Define the MongoDB connection string
# # # MONGODB_SERVER = "mongodb+srv://test123:test123@cluster0.uy9j5dp.mongodb.net/?appName=Cluster0"
# # # client = MongoClient(MONGODB_SERVER, tlsCAFile=certifi.where())

# # # # Initialize a new Flask web application
# # # app = Flask(__name__)
# # # CORS(app, origins=["http://localhost:5173", "http://127.0.0.1:5173"], supports_credentials=True)

# # # # Route for user login
# # # @app.route('/login', methods=['POST'])
# # # def login():
# # #     data = request.get_json()
# # #     userId = data.get("userId")
# # #     password = data.get("password")

# # #     if not userId or not password:
# # #         return jsonify({
# # #             "success": False,
# # #             "message": "Missing userId or password"
# # #         }), 400

# # #     # Use usersDatabase.login
# # #     result = usersDatabase.login(client, userId, password)
# # #     if result is True:
# # #         return jsonify({
# # #             "success": True,
# # #             "message": "Login successful"
# # #         })
# # #     elif result == "incorrect_password":
# # #         return jsonify({
# # #             "success": False,
# # #             "message": "Incorrect password"
# # #         }), 401
# # #     else:
# # #         return jsonify({
# # #             "success": False,
# # #             "message": "User does not exist"
# # #         }), 404

# # # # Route for the main page (Work in progress)
# # # @app.route('/main', methods=['POST'])
# # # def mainPage():
# # #     data = request.get_json()
# # #     userId = data.get("userId")
# # #     if not userId:
# # #         return jsonify({"success": False, "message": "Missing userId"}), 400
# # #     projects = usersDatabase.getUserProjectsList(client, userId)
# # #     return jsonify({"success": True, "projects": projects})

# # # # Route for joining a project
# # # @app.route('/join_project', methods=['POST'])
# # # def join_project():
# # #     data = request.get_json()
# # #     userId = data.get("userId")
# # #     projectId = data.get("projectId")
# # #     if not userId or not projectId:
# # #         return jsonify({"success": False, "message": "Missing userId or projectId"}), 400
# # #     result = usersDatabase.joinProject(client, userId, projectId)
# # #     if result:
# # #         return jsonify({"success": True, "message": "Joined project successfully"})
# # #     else:
# # #         return jsonify({"success": False, "message": "Failed to join project"}), 400

# # # # Route for adding a new user
# # # @app.route('/add_user', methods=['POST'])
# # # def add_user():
# # #     data = request.get_json()
# # #     userId = data.get("userId")
# # #     password = data.get("password")

# # #     if not userId or not password:
# # #         return jsonify({
# # #             "success": False,
# # #             "message": "Missing userId or password"
# # #         }), 400

# # #     result = usersDatabase.addUser(client, userId, password)
# # #     if result:
# # #         return jsonify({
# # #             "success": True,
# # #             "message": "User added successfully"
# # #         })
# # #     else:
# # #         return jsonify({
# # #             "success": False,
# # #             "message": "User already exists"
# # #         }), 409

# # # # Route for getting the list of user projects
# # # @app.route('/get_user_projects_list', methods=['POST'])
# # # def get_user_projects_list():
# # #     data = request.get_json()
# # #     userId = data.get("userId")
# # #     if not userId:
# # #         return jsonify({"success": False, "message": "Missing userId"}), 400
# # #     projects = usersDatabase.getUserProjectsList(client, userId)
# # #     return jsonify({"success": True, "projects": projects})

# # # # Route for creating a new project
# # # @app.route('/create_project', methods=['POST'])
# # # def create_project():
# # #     data = request.get_json()
# # #     projectName = data.get("projectName")
# # #     projectId = data.get("projectId")
# # #     description = data.get("description")
# # #     if not projectName or not projectId or not description:
# # #         return jsonify({"success": False, "message": "Missing projectName, projectId, or description"}), 400
# # #     result = projectsDB.createProject(client, projectName, projectId, description)
# # #     if result:
# # #         return jsonify({"success": True, "message": "Project created successfully"})
# # #     else:
# # #         return jsonify({"success": False, "message": "Project already exists or failed to create"}), 409

# # # # Route for getting project information
# # # @app.route('/get_project_info', methods=['POST'])
# # # def get_project_info():
# # #     data = request.get_json()
# # #     projectId = data.get("projectId")
# # #     if not projectId:
# # #         return jsonify({"success": False, "message": "Missing projectId"}), 400
# # #     project = projectsDB.queryProject(client, projectId)
# # #     if project:
# # #         return jsonify({"success": True, "project": project})
# # #     else:
# # #         return jsonify({"success": False, "message": "Project not found"}), 404

# # # # Route for getting all hardware names
# # # @app.route('/get_all_hw_names', methods=['POST'])
# # # def get_all_hw_names():
# # #     hw_names = hardwareDB.getAllHwNames(client)
# # #     return jsonify({"success": True, "hardwareNames": hw_names})

# # # # Route for getting hardware information
# # # @app.route('/get_hw_info', methods=['POST'])
# # # def get_hw_info():
# # #     data = request.get_json()
# # #     hwSetName = data.get("hwSetName")
# # #     if not hwSetName:
# # #         return jsonify({"success": False, "message": "Missing hwSetName"}), 400
# # #     hw_info = hardwareDB.queryHardwareSet(client, hwSetName)
# # #     if hw_info:
# # #         return jsonify({"success": True, "hardware": hw_info})
# # #     else:
# # #         return jsonify({"success": False, "message": "Hardware set not found"}), 404

# # # # Route for checking out hardware
# # # @app.route('/check_out', methods=['POST'])
# # # def check_out():
# # #     data = request.get_json()
# # #     projectId = data.get("projectId")
# # #     hwSetName = data.get("hwSetName")
# # #     qty = data.get("qty")
# # #     userId = data.get("userId")
# # #     if not projectId or not hwSetName or qty is None or not userId:
# # #         return jsonify({"success": False, "message": "Missing projectId, hwSetName, qty, or userId"}), 400
# # #     result = projectsDB.checkOutHW(client, projectId, hwSetName, qty, userId)
# # #     if result:
# # #         return jsonify({"success": True, "message": "Checked out hardware successfully"})
# # #     else:
# # #         return jsonify({"success": False, "message": "Failed to check out hardware"}), 400

# # # # Route for checking in hardware
# # # @app.route('/check_in', methods=['POST'])
# # # def check_in():
# # #     data = request.get_json()
# # #     projectId = data.get("projectId")
# # #     hwSetName = data.get("hwSetName")
# # #     qty = data.get("qty")
# # #     userId = data.get("userId")
# # #     if not projectId or not hwSetName or qty is None or not userId:
# # #         return jsonify({"success": False, "message": "Missing projectId, hwSetName, qty, or userId"}), 400
# # #     result = projectsDB.checkInHW(client, projectId, hwSetName, qty, userId)
# # #     if result:
# # #         return jsonify({"success": True, "message": "Checked in hardware successfully"})
# # #     else:
# # #         return jsonify({"success": False, "message": "Failed to check in hardware"}), 400

# # # # Route for creating a new hardware set
# # # @app.route('/create_hardware_set', methods=['POST'])
# # # def create_hardware_set():
# # #     data = request.get_json()
# # #     hwSetName = data.get("hwSetName")
# # #     initCapacity = data.get("initCapacity")
# # #     if not hwSetName or initCapacity is None:
# # #         return jsonify({"success": False, "message": "Missing hwSetName or initCapacity"}), 400
# # #     result = hardwareDB.createHardwareSet(client, hwSetName, initCapacity)
# # #     if result:
# # #         return jsonify({"success": True, "message": "Hardware set created successfully"})
# # #     else:
# # #         return jsonify({"success": False, "message": "Failed to create hardware set"}), 400

# # # # Route for checking the inventory of projects
# # # @app.route('/api/inventory', methods=['GET'])
# # # def check_inventory():
# # #     db = client["HaaS_DB"]
# # #     projects = db["projects"].find()
# # #     project_list = []
# # #     for project in projects:
# # #         project["_id"] = str(project["_id"])
# # #         project_list.append(project)
# # #     return jsonify({"success": True, "projects": project_list})

# # # # Main entry point for the application
# # # if __name__ == '__main__':
# # #     app.run(debug=True, host='0.0.0.0', port=5000)

# # import os
# # import certifi

# # from flask import Flask, request, jsonify
# # from pymongo import MongoClient
# # from flask_cors import CORS

# # import usersDatabase
# # import projectsDB
# # import hardwareDB


# # MONGODB_SERVER = os.environ.get("MONGODB_SERVER")
# # if not MONGODB_SERVER:
# #     raise ValueError("MONGODB_SERVER environment variable is not set")

# # FRONTEND_URL = os.environ.get("FRONTEND_URL", "http://localhost:5173")

# # client = MongoClient(MONGODB_SERVER, tlsCAFile=certifi.where())

# # app = Flask(__name__)

# # CORS(
# #     app,
# #     origins=[
# #         "http://localhost:5173",
# #         "http://127.0.0.1:5173",
# #         FRONTEND_URL,
# #     ],
# #     supports_credentials=True,
# # )


# # @app.route("/health", methods=["GET"])
# # def health():
# #     return jsonify({"success": True, "message": "Backend is running"}), 200


# # @app.route('/login', methods=['POST'])
# # def login():
# #     data = request.get_json() or {}
# #     userId = data.get("userId")
# #     password = data.get("password")

# #     if not userId or not password:
# #         return jsonify({
# #             "success": False,
# #             "message": "Missing userId or password"
# #         }), 400

# #     result = usersDatabase.login(client, userId, password)
# #     if result is True:
# #         return jsonify({
# #             "success": True,
# #             "message": "Login successful"
# #         }), 200
# #     elif result == "incorrect_password":
# #         return jsonify({
# #             "success": False,
# #             "message": "Incorrect password"
# #         }), 401
# #     else:
# #         return jsonify({
# #             "success": False,
# #             "message": "User does not exist"
# #         }), 404


# # @app.route('/main', methods=['POST'])
# # def mainPage():
# #     data = request.get_json() or {}
# #     userId = data.get("userId")
# #     if not userId:
# #         return jsonify({"success": False, "message": "Missing userId"}), 400
# #     projects = usersDatabase.getUserProjectsList(client, userId)
# #     return jsonify({"success": True, "projects": projects}), 200


# # @app.route('/join_project', methods=['POST'])
# # def join_project():
# #     data = request.get_json() or {}
# #     userId = data.get("userId")
# #     projectId = data.get("projectId")
# #     if not userId or not projectId:
# #         return jsonify({"success": False, "message": "Missing userId or projectId"}), 400

# #     result = usersDatabase.joinProject(client, userId, projectId)
# #     if result:
# #         return jsonify({"success": True, "message": "Joined project successfully"}), 200
# #     else:
# #         return jsonify({"success": False, "message": "Failed to join project"}), 400


# # @app.route('/add_user', methods=['POST'])
# # def add_user():
# #     data = request.get_json() or {}
# #     userId = data.get("userId")
# #     password = data.get("password")

# #     if not userId or not password:
# #         return jsonify({
# #             "success": False,
# #             "message": "Missing userId or password"
# #         }), 400

# #     result = usersDatabase.addUser(client, userId, password)
# #     if result:
# #         return jsonify({
# #             "success": True,
# #             "message": "User added successfully"
# #         }), 201
# #     else:
# #         return jsonify({
# #             "success": False,
# #             "message": "User already exists"
# #         }), 409


# # @app.route('/get_user_projects_list', methods=['POST'])
# # def get_user_projects_list():
# #     data = request.get_json() or {}
# #     userId = data.get("userId")
# #     if not userId:
# #         return jsonify({"success": False, "message": "Missing userId"}), 400
# #     projects = usersDatabase.getUserProjectsList(client, userId)
# #     return jsonify({"success": True, "projects": projects}), 200


# # @app.route('/create_project', methods=['POST'])
# # def create_project():
# #     data = request.get_json() or {}
# #     projectName = data.get("projectName")
# #     projectId = data.get("projectId")
# #     description = data.get("description")

# #     if not projectName or not projectId or not description:
# #         return jsonify({"success": False, "message": "Missing projectName, projectId, or description"}), 400

# #     result = projectsDB.createProject(client, projectName, projectId, description)
# #     if result:
# #         return jsonify({"success": True, "message": "Project created successfully"}), 201
# #     else:
# #         return jsonify({"success": False, "message": "Project already exists or failed to create"}), 409


# # @app.route('/get_project_info', methods=['POST'])
# # def get_project_info():
# #     data = request.get_json() or {}
# #     projectId = data.get("projectId")
# #     if not projectId:
# #         return jsonify({"success": False, "message": "Missing projectId"}), 400

# #     project = projectsDB.queryProject(client, projectId)
# #     if project:
# #         return jsonify({"success": True, "project": project}), 200
# #     else:
# #         return jsonify({"success": False, "message": "Project not found"}), 404


# # @app.route('/get_all_hw_names', methods=['POST'])
# # def get_all_hw_names():
# #     hw_names = hardwareDB.getAllHwNames(client)
# #     return jsonify({"success": True, "hardwareNames": hw_names}), 200


# # @app.route('/get_hw_info', methods=['POST'])
# # def get_hw_info():
# #     data = request.get_json() or {}
# #     hwSetName = data.get("hwSetName")
# #     if not hwSetName:
# #         return jsonify({"success": False, "message": "Missing hwSetName"}), 400

# #     hw_info = hardwareDB.queryHardwareSet(client, hwSetName)
# #     if hw_info:
# #         return jsonify({"success": True, "hardware": hw_info}), 200
# #     else:
# #         return jsonify({"success": False, "message": "Hardware set not found"}), 404


# # @app.route('/check_out', methods=['POST'])
# # def check_out():
# #     data = request.get_json() or {}
# #     projectId = data.get("projectId")
# #     hwSetName = data.get("hwSetName")
# #     qty = data.get("qty")
# #     userId = data.get("userId")

# #     if not projectId or not hwSetName or qty is None or not userId:
# #         return jsonify({"success": False, "message": "Missing projectId, hwSetName, qty, or userId"}), 400

# #     try:
# #         qty = int(qty)
# #     except (TypeError, ValueError):
# #         return jsonify({"success": False, "message": "qty must be an integer"}), 400

# #     if qty <= 0:
# #         return jsonify({"success": False, "message": "qty must be greater than 0"}), 400

# #     result = projectsDB.checkOutHW(client, projectId, hwSetName, qty, userId)
# #     if result:
# #         return jsonify({"success": True, "message": "Checked out hardware successfully"}), 200
# #     else:
# #         return jsonify({"success": False, "message": "Failed to check out hardware"}), 400


# # @app.route('/check_in', methods=['POST'])
# # def check_in():
# #     data = request.get_json() or {}
# #     projectId = data.get("projectId")
# #     hwSetName = data.get("hwSetName")
# #     qty = data.get("qty")
# #     userId = data.get("userId")

# #     if not projectId or not hwSetName or qty is None or not userId:
# #         return jsonify({"success": False, "message": "Missing projectId, hwSetName, qty, or userId"}), 400

# #     try:
# #         qty = int(qty)
# #     except (TypeError, ValueError):
# #         return jsonify({"success": False, "message": "qty must be an integer"}), 400

# #     if qty <= 0:
# #         return jsonify({"success": False, "message": "qty must be greater than 0"}), 400

# #     result = projectsDB.checkInHW(client, projectId, hwSetName, qty, userId)
# #     if result:
# #         return jsonify({"success": True, "message": "Checked in hardware successfully"}), 200
# #     else:
# #         return jsonify({"success": False, "message": "Failed to check in hardware"}), 400


# # @app.route('/create_hardware_set', methods=['POST'])
# # def create_hardware_set():
# #     data = request.get_json() or {}
# #     hwSetName = data.get("hwSetName")
# #     initCapacity = data.get("initCapacity")

# #     if not hwSetName or initCapacity is None:
# #         return jsonify({"success": False, "message": "Missing hwSetName or initCapacity"}), 400

# #     try:
# #         initCapacity = int(initCapacity)
# #     except (TypeError, ValueError):
# #         return jsonify({"success": False, "message": "initCapacity must be an integer"}), 400

# #     if initCapacity < 0:
# #         return jsonify({"success": False, "message": "initCapacity cannot be negative"}), 400

# #     result = hardwareDB.createHardwareSet(client, hwSetName, initCapacity)
# #     if result:
# #         return jsonify({"success": True, "message": "Hardware set created successfully"}), 201
# #     else:
# #         return jsonify({"success": False, "message": "Failed to create hardware set"}), 400


# # @app.route('/api/inventory', methods=['GET'])
# # def check_inventory():
# #     db = client["HaaS_DB"]
# #     projects = db["projects"].find()
# #     project_list = []
# #     for project in projects:
# #         project["_id"] = str(project["_id"])
# #         project_list.append(project)
# #     return jsonify({"success": True, "projects": project_list}), 200


# # if __name__ == '__main__':
# #     app.run(debug=True, host='0.0.0.0', port=5000)

# import os
# import certifi

# from flask import Flask, request, jsonify
# from pymongo import MongoClient
# from flask_cors import CORS

# import usersDatabase
# import projectsDB
# import hardwareDB


# MONGODB_SERVER = os.environ.get("MONGODB_SERVER")
# if not MONGODB_SERVER:
#     raise ValueError("MONGODB_SERVER environment variable is not set")

# FRONTEND_URL = os.environ.get("FRONTEND_URL", "http://localhost:5173")

# client = MongoClient(MONGODB_SERVER, tlsCAFile=certifi.where())

# app = Flask(__name__)

# CORS(
#     app,
#     origins=[
#         "http://localhost:5173",
#         "http://127.0.0.1:5173",
#         FRONTEND_URL,
#     ],
#     supports_credentials=True,
# )


# @app.route("/health", methods=["GET"])
# def health():
#     return jsonify({"success": True, "message": "Backend is running"}), 200


# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json() or {}
#     userId = data.get("userId")
#     password = data.get("password")

#     if not userId or not password:
#         return jsonify({
#             "success": False,
#             "message": "Missing userId or password"
#         }), 400

#     result = usersDatabase.login(client, userId, password)
#     if result is True:
#         return jsonify({
#             "success": True,
#             "message": "Login successful"
#         }), 200
#     elif result == "incorrect_password":
#         return jsonify({
#             "success": False,
#             "message": "Incorrect password"
#         }), 401
#     else:
#         return jsonify({
#             "success": False,
#             "message": "User does not exist"
#         }), 404


# @app.route('/main', methods=['POST'])
# def mainPage():
#     data = request.get_json() or {}
#     userId = data.get("userId")
#     if not userId:
#         return jsonify({"success": False, "message": "Missing userId"}), 400
#     projects = usersDatabase.getUserProjectsList(client, userId)
#     return jsonify({"success": True, "projects": projects}), 200


# @app.route('/join_project', methods=['POST'])
# def join_project():
#     data = request.get_json() or {}
#     userId = data.get("userId")
#     projectId = data.get("projectId")

#     if not userId or not projectId:
#         return jsonify({"success": False, "message": "Missing userId or projectId"}), 400

#     result = usersDatabase.joinProject(client, userId, projectId)
#     if result:
#         return jsonify({"success": True, "message": "Joined project successfully"}), 200
#     else:
#         return jsonify({"success": False, "message": "Failed to join project"}), 400


# @app.route('/add_user', methods=['POST'])
# def add_user():
#     data = request.get_json() or {}
#     userId = data.get("userId")
#     password = data.get("password")

#     if not userId or not password:
#         return jsonify({
#             "success": False,
#             "message": "Missing userId or password"
#         }), 400

#     result = usersDatabase.addUser(client, userId, password)
#     if result:
#         return jsonify({
#             "success": True,
#             "message": "User added successfully"
#         }), 201
#     else:
#         return jsonify({
#             "success": False,
#             "message": "User already exists"
#         }), 409


# @app.route('/get_user_projects_list', methods=['POST'])
# def get_user_projects_list():
#     data = request.get_json() or {}
#     userId = data.get("userId")
#     if not userId:
#         return jsonify({"success": False, "message": "Missing userId"}), 400
#     projects = usersDatabase.getUserProjectsList(client, userId)
#     return jsonify({"success": True, "projects": projects}), 200


# @app.route('/create_project', methods=['POST'])
# def create_project():
#     data = request.get_json() or {}
#     projectName = data.get("projectName")
#     projectId = data.get("projectId")
#     description = data.get("description")
#     userId = data.get("userId")

#     if not projectName or not projectId or not description or not userId:
#         return jsonify({
#             "success": False,
#             "message": "Missing projectName, projectId, description, or userId"
#         }), 400

#     result = projectsDB.createProject(client, projectName, projectId, description)
#     if not result:
#         return jsonify({
#             "success": False,
#             "message": "Project already exists or failed to create"
#         }), 409

#     joined = usersDatabase.joinProject(client, userId, projectId)
#     if not joined:
#         return jsonify({
#             "success": False,
#             "message": "Project created, but failed to add creator to project"
#         }), 500

#     return jsonify({
#         "success": True,
#         "message": "Project created successfully"
#     }), 201


# @app.route('/get_project_info', methods=['POST'])
# def get_project_info():
#     data = request.get_json() or {}
#     projectId = data.get("projectId")
#     if not projectId:
#         return jsonify({"success": False, "message": "Missing projectId"}), 400

#     project = projectsDB.queryProject(client, projectId)
#     if project:
#         return jsonify({"success": True, "project": project}), 200
#     else:
#         return jsonify({"success": False, "message": "Project not found"}), 404


# @app.route('/get_all_hw_names', methods=['POST'])
# def get_all_hw_names():
#     hw_names = hardwareDB.getAllHwNames(client)
#     return jsonify({"success": True, "hardwareNames": hw_names}), 200


# @app.route('/get_hw_info', methods=['POST'])
# def get_hw_info():
#     data = request.get_json() or {}
#     hwSetName = data.get("hwSetName")
#     if not hwSetName:
#         return jsonify({"success": False, "message": "Missing hwSetName"}), 400

#     hw_info = hardwareDB.queryHardwareSet(client, hwSetName)
#     if hw_info:
#         return jsonify({"success": True, "hardware": hw_info}), 200
#     else:
#         return jsonify({"success": False, "message": "Hardware set not found"}), 404


# @app.route('/check_out', methods=['POST'])
# def check_out():
#     data = request.get_json() or {}
#     projectId = data.get("projectId")
#     hwSetName = data.get("hwSetName")
#     qty = data.get("qty")
#     userId = data.get("userId")

#     if not projectId or not hwSetName or qty is None or not userId:
#         return jsonify({"success": False, "message": "Missing projectId, hwSetName, qty, or userId"}), 400

#     try:
#         qty = int(qty)
#     except (TypeError, ValueError):
#         return jsonify({"success": False, "message": "qty must be an integer"}), 400

#     if qty <= 0:
#         return jsonify({"success": False, "message": "qty must be greater than 0"}), 400

#     result = projectsDB.checkOutHW(client, projectId, hwSetName, qty, userId)
#     if result:
#         return jsonify({"success": True, "message": "Checked out hardware successfully"}), 200
#     else:
#         return jsonify({"success": False, "message": "Failed to check out hardware"}), 400


# @app.route('/check_in', methods=['POST'])
# def check_in():
#     data = request.get_json() or {}
#     projectId = data.get("projectId")
#     hwSetName = data.get("hwSetName")
#     qty = data.get("qty")
#     userId = data.get("userId")

#     if not projectId or not hwSetName or qty is None or not userId:
#         return jsonify({"success": False, "message": "Missing projectId, hwSetName, qty, or userId"}), 400

#     try:
#         qty = int(qty)
#     except (TypeError, ValueError):
#         return jsonify({"success": False, "message": "qty must be an integer"}), 400

#     if qty <= 0:
#         return jsonify({"success": False, "message": "qty must be greater than 0"}), 400

#     result = projectsDB.checkInHW(client, projectId, hwSetName, qty, userId)
#     if result:
#         return jsonify({"success": True, "message": "Checked in hardware successfully"}), 200
#     else:
#         return jsonify({"success": False, "message": "Failed to check in hardware"}), 400


# @app.route('/create_hardware_set', methods=['POST'])
# def create_hardware_set():
#     data = request.get_json() or {}
#     hwSetName = data.get("hwSetName")
#     initCapacity = data.get("initCapacity")

#     if not hwSetName or initCapacity is None:
#         return jsonify({"success": False, "message": "Missing hwSetName or initCapacity"}), 400

#     try:
#         initCapacity = int(initCapacity)
#     except (TypeError, ValueError):
#         return jsonify({"success": False, "message": "initCapacity must be an integer"}), 400

#     if initCapacity < 0:
#         return jsonify({"success": False, "message": "initCapacity cannot be negative"}), 400

#     result = hardwareDB.createHardwareSet(client, hwSetName, initCapacity)
#     if result:
#         return jsonify({"success": True, "message": "Hardware set created successfully"}), 201
#     else:
#         return jsonify({"success": False, "message": "Failed to create hardware set"}), 400


# @app.route('/api/inventory', methods=['GET'])
# def check_inventory():
#     db = client["HaaS_DB"]
#     projects = db["projects"].find()
#     project_list = []
#     for project in projects:
#         project["_id"] = str(project["_id"])
#         project_list.append(project)
#     return jsonify({"success": True, "projects": project_list}), 200


# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

import usersDatabase
import projectsDB
import hardwareDB

app = Flask(__name__)

FRONTEND_ORIGIN = os.environ.get("FRONTEND_ORIGIN", "http://localhost:5173")
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")

# CORS(
#     app,
#     supports_credentials=True,
#     origins=[FRONTEND_ORIGIN, "http://localhost:5173", "http://127.0.0.1:5173"]
# )
CORS(
    app,
    supports_credentials=True,
    origins=[
        FRONTEND_ORIGIN,
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ]
)

client = MongoClient(MONGO_URI)


@app.route("/")
def home():
    return jsonify({"success": True, "message": "HaaS backend is running"})


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    user_id = (data.get("userId") or "").strip()
    password = data.get("password") or ""

    if not user_id or not password:
        return jsonify({"success": False, "message": "Missing userId or password"}), 400

    result = usersDatabase.login(client, user_id, password)

    if result is True:
        return jsonify({
            "success": True,
            "message": "Login successful",
            "user": {"userId": user_id}
        })

    if result == "incorrect_password":
        return jsonify({"success": False, "message": "Incorrect password"}), 401

    return jsonify({"success": False, "message": "User does not exist"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json() or {}
    user_id = (data.get("userId") or "").strip()
    password = data.get("password") or ""

    if not user_id or not password:
        return jsonify({"success": False, "message": "Missing userId or password"}), 400

    created = usersDatabase.addUser(client, user_id, password)

    if not created:
        return jsonify({"success": False, "message": "User already exists"}), 400

    return jsonify({"success": True, "message": "User created successfully"})


@app.route("/join_project", methods=["POST"])
def join_project():
    data = request.get_json() or {}
    user_id = (data.get("userId") or "").strip()
    project_id = (data.get("projectId") or "").strip()

    if not user_id or not project_id:
        return jsonify({"success": False, "message": "Missing userId or projectId"}), 400

    joined = usersDatabase.joinProject(client, user_id, project_id)

    if not joined:
        return jsonify({"success": False, "message": "User or project not found"}), 404

    return jsonify({"success": True, "message": "Joined project successfully"})


@app.route("/get_user_projects_list", methods=["POST"])
def get_user_projects_list():
    data = request.get_json() or {}
    user_id = (data.get("userId") or "").strip()

    if not user_id:
        return jsonify({"success": False, "message": "Missing userId"}), 400

    projects = usersDatabase.getUserProjectsList(client, user_id)
    return jsonify({"success": True, "projects": projects})


@app.route("/create_project", methods=["POST"])
def create_project():
    data = request.get_json() or {}
    project_name = (data.get("projectName") or "").strip()
    project_id = (data.get("projectId") or "").strip()
    description = (data.get("description") or "").strip()
    user_id = (data.get("userId") or "").strip()

    if not project_name or not project_id or not user_id:
        return jsonify({"success": False, "message": "Missing required fields"}), 400

    created = projectsDB.createProject(client, project_name, project_id, description)
    if not created:
        return jsonify({"success": False, "message": "Project ID already exists"}), 400

    usersDatabase.joinProject(client, user_id, project_id)

    project = projectsDB.queryProject(client, project_id)

    return jsonify({
        "success": True,
        "message": "Project created successfully",
        "project": project
    })


@app.route("/get_project_info", methods=["POST"])
def get_project_info():
    data = request.get_json() or {}
    project_id = (data.get("projectId") or "").strip()

    if not project_id:
        return jsonify({"success": False, "message": "Missing projectId"}), 400

    project = projectsDB.queryProject(client, project_id)

    if not project:
        return jsonify({"success": False, "message": "Project not found"}), 404

    return jsonify({"success": True, "project": project})


@app.route("/get_all_hw_names", methods=["POST"])
def get_all_hw_names():
    names = hardwareDB.getAllHwNames(client)
    return jsonify({"success": True, "hardwareNames": names})


@app.route("/get_hw_info", methods=["POST"])
def get_hw_info():
    data = request.get_json() or {}
    hw_set_name = (data.get("hwSetName") or "").strip()

    if not hw_set_name:
        return jsonify({"success": False, "message": "Missing hwSetName"}), 400

    hw = hardwareDB.queryHardwareSet(client, hw_set_name)
    if not hw:
        return jsonify({"success": False, "message": "Hardware set not found"}), 404

    return jsonify({
        "success": True,
        "hardware": {
            "hwSetName": hw.get("hwName"),
            "capacity": hw.get("capacity", 0),
            "availability": hw.get("availability", 0),
            "available": hw.get("availability", 0)
        }
    })


@app.route("/check_out", methods=["POST"])
def check_out():
    data = request.get_json() or {}
    project_id = (data.get("projectId") or "").strip()
    hw_set_name = (data.get("hwSetName") or "").strip()
    user_id = (data.get("userId") or "").strip()

    try:
        qty = int(data.get("qty", 0))
    except (TypeError, ValueError):
        qty = 0

    if not project_id or not hw_set_name or not user_id or qty < 1:
        return jsonify({"success": False, "message": "Invalid request data"}), 400

    success, message = projectsDB.checkOutHW(client, project_id, hw_set_name, qty, user_id)

    status = 200 if success else 400
    return jsonify({"success": success, "message": message}), status


@app.route("/check_in", methods=["POST"])
def check_in():
    data = request.get_json() or {}
    project_id = (data.get("projectId") or "").strip()
    hw_set_name = (data.get("hwSetName") or "").strip()
    user_id = (data.get("userId") or "").strip()

    try:
        qty = int(data.get("qty", 0))
    except (TypeError, ValueError):
        qty = 0

    if not project_id or not hw_set_name or not user_id or qty < 1:
        return jsonify({"success": False, "message": "Invalid request data"}), 400

    success, message = projectsDB.checkInHW(client, project_id, hw_set_name, qty, user_id)

    status = 200 if success else 400
    return jsonify({"success": success, "message": message}), status


@app.route("/create_hardware_set", methods=["POST"])
def create_hardware_set():
    data = request.get_json() or {}
    hw_set_name = (data.get("hwSetName") or "").strip()

    try:
        init_capacity = int(data.get("capacity", 0))
    except (TypeError, ValueError):
        init_capacity = 0

    if not hw_set_name or init_capacity < 0:
        return jsonify({"success": False, "message": "Invalid hardware set data"}), 400

    created = hardwareDB.createHardwareSet(client, hw_set_name, init_capacity)

    if not created:
        return jsonify({"success": False, "message": "Hardware set already exists"}), 400

    return jsonify({"success": True, "message": "Hardware set created successfully"})


@app.route("/api/inventory", methods=["GET"])
def inventory():
    db = client["HaaS_DB"]
    projects = db["projects"].find()

    inventory_data = []
    for project in projects:
        inventory_data.append({
            "projectId": project.get("projectId"),
            "projectName": project.get("projectName"),
            "description": project.get("description", ""),
            "hwSets": project.get("hwSets", {}),
            "users": project.get("users", [])
        })

    return jsonify({"success": True, "inventory": inventory_data})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)