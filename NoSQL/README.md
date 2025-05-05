# MongoDB Scripts

This directory contains MongoDB scripts for database operations.

## Scripts

### 0-list_databases
Lists all databases in the MongoDB server.

Usage:
```bash
./0-list_databases
```

Example output:
```
admin   0.000GB
config  0.000GB
local   0.000GB
```

### 1-use_or_create_database
Creates or switches to a database named `my_db`.

Usage:
```bash
./1-use_or_create_database
```

Example output:
```
switched to db my_db
```

## Requirements

- MongoDB server must be running
- Scripts must be executable (`chmod +x script_name`)
- Scripts must use the correct MongoDB comment format (`// comment`)
- Scripts must have a shebang line (`#!/usr/bin/env mongo`)

## Author
Nour Kasmi 