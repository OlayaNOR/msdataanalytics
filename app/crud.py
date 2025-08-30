from .database import collection

def insert_package(package: dict):
    collection.insert_one(package)

def get_packages_grouped():
    pipeline = [
        {"$group": {"_id": "$estado", "count": {"$sum": 1}}}
    ]
    return list(collection.aggregate(pipeline))