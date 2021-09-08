#!/usr/bin/env python3
"""
function that returns the list of schools having specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    return result of search string topic in collection
    """
    query_topic = {'topics': topic}
    if mongo_collection:
        return mongo_collection.find(query_topic)


if __name__ == "__main__":
    schools_by_topic(mongo_collection, topic)
