#!/usr/bin/env python3
"""
function that updates a document in collection (mongo)
"""


def update_topics(mongo_collection, name, topics):
    """
    return new id of the newly inserted document
    """
    query_name = {'name': name}
    new_topics = {'$set': {'topics': topics}}
    if mongo_collection:
        return mongo_collection.update_many(query_name, new_topics)


if __name__ == "__main__":
    update_topics(mongo_collection, name, topics)
