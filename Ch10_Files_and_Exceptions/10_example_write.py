# Python Crash Course, Eric Matthes, no starch press
# Ch10 Files and Exceptions
# Textbook Exercises

# Louis Lozano
# 06-20-2019
# 10_example_write.py

# Python Version: 3.5.3
# Description: Creates a text file and writes lines of text to it.

filename = 'programming.txt'

# Opens a file in 'write' mode which erases it's contents and allows you to
#   write to the file.
with open(filename, 'w') as file_object:
    file_object.write('I love programming.\n')
    file_object.write('I love creating new games.\n')
