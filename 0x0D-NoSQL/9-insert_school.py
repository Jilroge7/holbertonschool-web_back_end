#!/usr/bin/env python3
"""
function that inserts a new document in collection (mongo)
"""


def insert_school(mongo_collection, **kwargs):
    """
    return new id of the newly inserted document
    """
    if mongo_collection:
        return mongo_collection.insert_one(kwargs).inserted_id


if __name__ == "__main__":
    insert_school(mongo_collection, **kwargs)
