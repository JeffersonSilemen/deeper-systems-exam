from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://recruiter:recruiter@cluster0.duc2zqo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
try:
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["Cluster0"]
    collection = db["users"]
except Exception as e:
    print(e)
