# Python Crash Course, Eric Matthes, no starch press
# Ch5 if statements
# Textbook Exercises

# Louis Lozano
# 3-6-2019
# if_else_list.py

usernames = ['admin', 'tim', 'jessica', 'david', 'mary']
# usernames = []

# Checks if list is empty. Returns true if list is not empty
# and returns false if list is empty.
if usernames:
    # Loops through list Checks a conditional statment for each item
    # in the list. Prints appropriate statment for each item.
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + username + ", thank you for loggin in.")
# Runs if list is empty.
else:
    print("We need to find some users!")
