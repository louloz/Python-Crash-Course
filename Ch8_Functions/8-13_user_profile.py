# Python Crash Course, Eric Matthes, no starch press
# Ch8 Functions
# Textbook Exercises

# Louis Lozano
# 3-22-2019
# 8-13_user_profile.py

# Description: A function that accepts any amount of key-value pairs
#   and creates a dictionary with information about the user.
#   The function is called to create a user profile.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about the user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    # A for loop that takes all key value pairs passed to the parameter and
    #   stores them in the dictionary 'profile'.
    for key, value in user_info.items():
        profile[key] = value

    # Returns the dictionary.
    return profile

# The function is called to build a user profile.
user_profile = build_profile('louie', 'lozano',
                             location='colorado',
                             field='games')

# Prints the user profile.
print(user_profile)
