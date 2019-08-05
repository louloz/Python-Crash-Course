# Python Crash Course, Eric Matthes, no starch press
# Ch10 Files and Exceptions
# Textbook Exercises

# Louis Lozano
# 07-06-2019
# 10-12_favorite_number_remembered.py

# Python Version: 3.5.3

# Description: Loads a favorite number from a file and prints it. If
#   FileNotFoundError occurs, prompts user for their favorite number and saves
#   it.

import json

filename = 'favorite_number_remembered.json'

def load_num():
    '''Loads a favorite number from a file'''
    with open(filename) as f_obj:
        return json.load(f_obj)

def save_num():
    '''Prompts user for their favorite number and saves it to a file.'''
    fav_num = input('What\'s your favorite number? :')

    with open(filename, 'w') as f_obj:
        json.dump(fav_num, f_obj)
        print ('I\'ll remember your favorite number is ' + fav_num +
               ' for next time.')

try:
    fav_num = load_num()

except FileNotFoundError:
    save_num()

else:
    print('I know your favorite number! It\'s ' + fav_num + '.')

