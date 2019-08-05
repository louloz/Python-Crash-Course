# Python Crash Course, Eric Matthes, no starch press
# Ch6 Dictionaries
# Textbook Exercises

# Louis Lozano
# 04-01-2019
# 9-14_dice.py

# Python Version: 3.5.3
# Description: Imports the random module from the Python Standard Library and
#   uses the randint method to simulate a dice roll.

# Imports 
from random import randint

# Die class
class Die():
    '''Models a die.'''
    def __init__(self, sides=6):
        '''Initializes attribute.'''
        self.sides = sides

    def roll_die(self):
        '''Rolls the die.'''
        print(randint(1, self.sides))

# Creates an instance of a die.
my_die = Die()

# Rolls die 10 times.
for i in range(1, 11):
    my_die.roll_die()
