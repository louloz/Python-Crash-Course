# Python Crash Course, Eric Matthes, no starch press
# Ch8 Functions
# Textbook Exercises

# Louis Lozano
# 3-16-2019
# 8-3_t_shirt.py

# Description: A function that takes two parameters and uses them
#   to display a shirts' size and message printed on it.

def make_shirt(size, message):
    print('Shirt size: ' + size.title())
    print('Shirt message: ' + message)

# A function call using positional arguments.
make_shirt('medium', 'Hey!')

# A function call using keyword arguments.
make_shirt(message='Peace.', size='small')
