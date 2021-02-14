import json
import os
import time

import redis
from colorama import Fore, init

init()

# clears the screen for windows and linux
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Redis connection settings from redis.json
with open("redis.json", "r") as db:
    db = json.load(db)
    address = db.get("address")
    port = db.get("port")
    db_name = db.get("db")
    password = db.get("password")
    verbose = db.get("verbose")

print(f"\n{Fore.YELLOW}  Connecting to database...{Fore.RESET}")
time.sleep(1)

# Establish redis database connection
database = redis.Redis(host=(str(address)), port=port, db=db_name, password=password)

clear()

# Check if connection is established
try:
    database.ping()
    print(f"\n{Fore.GREEN}  Connected to database \n {Fore.RESET}")
except Exception as error:
    if verbose:
        print(f"\n{Fore.LIGHTRED_EX}  Unable to connect to database {Fore.RESET}")
        print(f"{Fore.LIGHTRED_EX}  Exception: {error} \n {Fore.RESET}")
        time.sleep(5)
    else:
        print(f"\n{Fore.LIGHTRED_EX}  Unable to connect to database \n {Fore.RESET}")
        time.sleep(5)
    exit(0)

# Name and content variables
name = input(f"{Fore.LIGHTWHITE_EX}Name: ")
content = input(f"{Fore.LIGHTWHITE_EX}Content: ")

# Set name and content in redis database
database.set(name, content)

# Prints the name and content from redis database
print(f"\n  {Fore.LIGHTBLUE_EX}{name} {Fore.LIGHTWHITE_EX}has content {Fore.LIGHTBLUE_EX}{database.get(name)}")
