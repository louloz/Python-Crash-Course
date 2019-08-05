# Python Crash Course, Eric Matthes, no starch press
# Ch10 Files and Exceptions
# Textbook Exercises

# Louis Lozano
# 07-04-2019
# 10-9_silent_cats_and_dogs.py

# Python Version: 3.5.3

# Description: Trys to open and read two files, printing their contents.
#   'try-except' blocks are use to fail silently instead of a printing a
#   python error message in case one of the files being opened is not found.

filename = 'cats.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()

except FileNotFoundError:
    pass

else:
    print(contents)

filename = 'dogs.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()

except FileNotFoundError:
    pass

else:
    print(contents)
