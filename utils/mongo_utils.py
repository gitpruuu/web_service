from pymongo import MongoClient


def get_collection(collection_name):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["web_service"]
    collection = db[collection_name]
    return collection
