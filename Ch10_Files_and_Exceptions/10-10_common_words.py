# Python Crash Course, Eric Matthes, no starch press
# Ch10 Files and Exceptions
# Textbook Exercises

# Louis Lozano
# 07-04-2019
# 10-10_common_words.py

# Python Version: 3.5.3

# Description: Reads a file and counts how many times the word 'the' appears in
#   it.

filename = 'cats.txt'

with open(filename) as file_object:
    contents = file_object.read()

    contents.lower().count('the')
