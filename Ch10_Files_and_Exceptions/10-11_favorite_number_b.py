# Python Crash Course, Eric Matthes, no starch press
# Ch10 Files and Exceptions
# Textbook Exercises

# Louis Lozano
# 07-06-2019
# 10-11_favorite_number_b.py

# Python Version: 3.5.3

# Description: Loads a favorite number from a file and prints it.

import json

filename = 'favorite_number.json'

with open(filename) as f_obj:
    fav_num = json.load(f_obj)

print('I know your favorite number! It\'s ' + fav_num + '.')
