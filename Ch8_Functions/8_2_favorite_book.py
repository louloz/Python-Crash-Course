# Python Crash Course, Eric Matthes, no starch press
# Ch8 Functions
# Textbook Exercises

# Louis Lozano
# 3-16-2019
# 8-2_favorite_book.py

# Description:A function that takes a parameter and uses it to
#   display a message.

# A function definition with a parameter.
def favorite_book(title):
    '''Takes value in parameter and puts it in a string.'''
    print('One of my favorite books is ' + title.title() + '.')

# A function call with an argument which is passed to the parameter.
favorite_book('Survivor')
