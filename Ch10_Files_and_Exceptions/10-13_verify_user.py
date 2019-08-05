# Python Crash Course, Eric Matthes, no starch press
# Ch10 Files and Exceptions
# Textbook Exercises

# Louis Lozano
# 07-06-2019
# 10-13_verify_user.py

# Python Version: 3.5.3

# Description: Loads stored username from a file and ask if it is the correct.
#   user. If the file does not exist, asks user for their username and stores
#   it. If the user says no it is not the correct user, ask the user for their
#   username and stores it. If the user says yes, greet the user.

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def verify_username(user):
    '''Checks if stored username is the current user. Returns yes or no'''
    is_user = input('Is ' + user + ' the correct username?')
    is_user = is_user.lower()
    return is_user

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        verify_usr = verify_username(username)
        if verify_usr == 'yes':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
