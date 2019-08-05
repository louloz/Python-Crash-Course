# Python Crash Course, Eric Matthes, no starch press
# Ch10 Files and Exceptions
# Textbook Exercises

# Louis Lozano
# 06-20-2019
# 10_example_1.py

# Python Version: 3.5.3

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
