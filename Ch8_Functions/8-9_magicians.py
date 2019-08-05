# Python Crash Course, Eric Matthes, no starch press
# Ch8 Functions
# Textbook Exercises

# Louis Lozano
# 3-20-2019
# 8-9_magicians.py

# Description: This program uses a function to take a list of magicians
#   and print their names one by one.

# Defines a function that takes a list of magician names and prints each
#   one in order.
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

# Defines a list of magicians.
magicians = ['david', 'chris', 'penn', 'teller', 'strange']

# Calls function with the list of magicians.
show_magicians(magicians)
