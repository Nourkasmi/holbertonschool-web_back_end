#!/usr/bin/env python3
"""
Provides statistics on Nginx logs stored in MongoDB.
This script connects to a MongoDB database and displays:
- Total number of logs
- Number of logs for each HTTP method
- Number of logs with GET method and /status path
"""
from pymongo import MongoClient


def log_stats():
    """
    Provides statistics on Nginx logs stored in MongoDB.
    Connects to the MongoDB server and prints:
    - Total number of logs
    - Number of logs for each HTTP method (GET, POST, PUT, PATCH, DELETE)
    - Number of logs with GET method and /status path
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
