# Python Crash Course, Eric Matthes, no starch press
# Ch10 Files and Exceptions
# Textbook Exercises

# Louis Lozano
# 07-06-2019
# 10-11_favorite_number.py

# Python Version: 3.5.3

# Description: Prompts user for their favorite number and stores it in a file.

# module used for storing and loading data.
import json

filename = 'favorite_number.json'

fav_num = input('What\'s your favorite number? :')

with open(filename, 'w') as f_obj:
    json.dump(fav_num, f_obj)
