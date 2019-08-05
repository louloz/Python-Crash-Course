# Python Crash Course, Eric Matthes, no starch press
# Ch10 Files and Exceptions
# Textbook Exercises

# Louis Lozano
# 06-20-2019
# 10-1_learning_python.py

# Python Version: 3.5.3
# Description: This program reads from a text file and prints it's contents
#   in 3 different ways.

# Stores the file name of the file we are working with in a varibale.
filename = 'learning_python.txt'

# Opens the file with 'file_object' representing the file.
# 'with' keyword is used to automatically close the file when it is no longer
# needed.
with open(filename) as file_object:
    # Reads file contents and stores it in the varibale 'contents'.
    contents = file_object.read()
    print(contents)

print()

with open(filename) as file_object:
    # Loops through the contents of the file line by line.
    for line in file_object:
        print(line.rstrip())

print()

with open(filename) as file_object:
    # 'readlines()' creates a list made up of each line in the text file and
    # stores it in a list called 'lines'.
    lines = file_object.readlines()

# Variable used to store the text within the file.
pi_string = ''

for line in lines:
    # Adds each line from the file into 'pi_string' one at a time.
    pi_string += line

print(pi_string)
print(len(pi_string))
