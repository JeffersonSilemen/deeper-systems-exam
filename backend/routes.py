from flask import Blueprint, request, jsonify
from bson import ObjectId
from config import collection
from models import User, UserPreferences
from dataclasses import asdict
from datetime import datetime

routes = Blueprint('routes', __name__)

# Render a message at the root URL
@routes.route("/")
def home():
    return "Server is running :)"

# List all users
@routes.route('/users', methods=['GET'])
def get_users():
    users = list(collection.find())
    for user in users:
        user['_id'] = str(user['_id'])
    return jsonify(users)

# Get a user by ID
@routes.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = collection.find_one({"_id": ObjectId(id)})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Create a new user
@routes.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(
        username=data["username"],
        password=data["password"],
        roles=data["roles"],
        preferences=UserPreferences(timezone=data["preferences"]["timezone"]),
        active=data.get("active", True),
        created_ts=data["created_ts"]
    )
    user_dict = asdict(new_user)
    inserted = collection.insert_one(user_dict)
    user_dict["_id"] = str(inserted.inserted_id)
    return jsonify({"message": "User created successfully"}), 201

# Update a user
@routes.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.json
    data["last_updated_at"] = datetime.now()
    update_data = {"$set": data}
    result = collection.update_one({"_id": ObjectId(id)}, update_data)

    if result.matched_count == 0:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify({"message": "User updated successfully"})

# Delete a user
@routes.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    result = collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify({"message": "User deleted successfully"})