# Python Crash Course, Eric Matthes, no starch press
# Ch10 Files and Exceptions
# Textbook Exercises

# Louis Lozano
# 06-21-2019
# 10-3_guest.py

# Python Version: 3.5.3
# Description: Prompts user for their name and writes it to a file called
#   'guest.txt'.

guest_name = input('What is your name?: ')

filename = 'guest.txt'

# The 'w' in the open method indicates the file is being opened in write mode.
#   This allows writing to the file. It also deletes the files contents when
#   the file is opened.
with open(filename, 'w') as file_object:
    file_object.write(guest_name)
