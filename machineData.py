from pymongo import MongoClient

# Replace the connection string with your MongoDB connection details
client = MongoClient("mongodb://localhost:27017/")
db = client["assetStats"]
