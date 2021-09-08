#!/usr/bin/env python3
"""
providing some stats about Nginx logs in MongoDb
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    doc_count = nginx_collection.count()
    get_post = nginx_collection.find()
    get_put = nginx_collection.find()
    get_patch = nginx_collection.find()
    get_delete = nginx_collection.find()
    stat = nginx_collection.find()

    print(f"{doc_count} logs")
    print("Methods:")
    print(f"\tmethod GET: {doc_count}")
    print(f"\tmethod POST: {get_post}")
    print(f"\tmethod PUT: {get_put}")
    print(f"\tmethod PATCH: {get_patch}")
    print(f"\tmethod DELETE: {get_delete}")
    print(f"{stat} status check")
