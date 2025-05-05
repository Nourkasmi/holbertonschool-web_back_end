# NoSQL - MongoDB Scripts

This directory contains MongoDB scripts for database operations.

## Files

### 0-list_databases
A script that lists all databases in MongoDB.
```bash
./0-list_databases | mongo
```
Example output:
```
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
admin        0.000GB
config       0.000GB
local        0.000GB
logs         0.005GB
bye
```

### 1-use_or_create_database
A script that creates or uses the database `my_db`.
```bash
./1-use_or_create_database | mongo
```
Example output:
```
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db my_db
bye
```

## Requirements
- MongoDB server (version 3.6.3 or higher)
- MongoDB shell
- Ubuntu 20.04 LTS

## Usage
All scripts are executable and can be run directly with the MongoDB shell:
```bash
./script_name | mongo
```

## Author
Nour Kasmi 