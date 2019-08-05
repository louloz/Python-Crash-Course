# Python Crash Course, Eric Matthes, no starch press
# Ch8 Functions
# Textbook Exercises

# Louis Lozano
# 3-22-2019
# 8-12_sandwiches.py

# Description: A function that takes any amount of sandwich items as it's
#   parameter which it stores in a tuple. It then uses the tuple to describe
#   the sandwich. 

# * indicates a tuple parameter that will take any number of items.
def sandwich(*items):
    print('Your sandwich will have the following items.')

    for item in items:
        print('\t- ' + item)

    print('\n')

sandwich('cheese')

sandwich('cheese', 'mushrooms')

sandwich('turkey', 'bell pepper', 'cheese')
