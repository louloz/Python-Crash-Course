# Python Crash Course, Eric Matthes, no starch press
# Ch5 if statements
# Textbook Exercises

# Louis Lozano
# 3-6-2019
# 5-10checking_usernames.py

current_users = ['ash', 'brock', 'misty', 'gary', 'oak']

new_users = ['May', 'surge', 'brOck', 'gary', 'cynthiA']

# Loops through new_users checking if each item is also in current_users
for new_user in new_users:
    # Comparison is case insensitive. new_user is checked in all lower case
    # like each item is in current_users.
    if new_user.lower() in current_users:
        print("That username is taken. You must enter a new username.")
    else:
        print("That username is available.")
