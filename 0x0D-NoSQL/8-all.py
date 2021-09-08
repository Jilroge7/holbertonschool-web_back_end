#!/usr/bin/env python3
"""
function that lists all documents in collection (mongo)
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    return empty list if no doc in collection
    mongo_collection is the pymongo collection obj
    """
    if mongo_collection:
        return mongo_collection.find()
    else:
        return []


if __name__ == "__main__":
    list_all(mongo_collection)
