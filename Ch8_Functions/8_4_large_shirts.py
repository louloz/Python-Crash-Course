# Python Crash Course, Eric Matthes, no starch press
# Ch8 Functions
# Textbook Exercises

# Louis Lozano
# 3-16-2019
# 8-4_large_shirts.py

# Description: A function that takes two parameters and uses them
#   to display a shirts' size and message printed on it. Both parameters
#   have default values.

# A function definition with default values for it's parameters.
def make_shirt(size='large', message='I love Python!'):
    print('Shirt size: ' + size.title())
    print('Shirt message: ' + message)

# A function call using positional arguments.
make_shirt('medium')

# A function call using keyword arguments.
make_shirt(message='Peace.')

# A function call using only the default values.
make_shirt()

