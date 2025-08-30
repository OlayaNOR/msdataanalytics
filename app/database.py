from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb://mongo:27017")
db = client["packages_db"]
collection = db["packages"]