import json
from dataclasses import asdict
from config import collection
from models import User, UserPreferences

# Function to parse the JSON file and return a list of User objects
def transform_user(data):
    roles = []
    if data.get("is_user_admin"):
        roles.append("admin")
    if data.get("is_user_manager"):
        roles.append("manager")
    if data.get("is_user_tester"):
        roles.append("tester")
    
    return User(
        username=data["user"],
        password=data["password"],
        roles=roles,
        preferences=UserPreferences(timezone=data["user_timezone"]),
        active=data.get("active", True),
        created_ts=data["created_at"]
    )

# Function to import data from JSON file into MongoDB
def import_data(json_file):
    with open(json_file, 'r', encoding="utf-8") as file:
        data = json.load(file)
    
    users = [transform_user(user) for user in data["users"]]

    # Insert data into MongoDB
    collection.insert_many([asdict(user) for user in users])
    print(f"Inserted {len(users)} users into the database.")
