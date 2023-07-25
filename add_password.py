"""Simple script to add hashed passwords to our json."""

import bcrypt
import json
from getpass import getpass

def main():
    print("Welcome to the Bubble Guppie's rudimentary password manager!")
    passwords_dict = {}
    with open("pass.json", "r+") as file:
        passwords_dict = json.load(file)
        username = input("Please enter a username: ")
        password = getpass()
        hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt(10))
        passwords_dict[username] = hashed_pw
        json.dump(passwords_dict, file)

if __name__ == "__main__":
    main()