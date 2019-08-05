# Python Crash Course, Eric Matthes, no starch press
# Ch8 Functions
# Textbook Exercises

# Louis Lozano
# 3-23-2019
# car_import.py

# Description: This program imports a function from the 'car_functions' module
#   and uses it to build a car profile.

# Imports one function from car_functions.py and gives it the alias 'bc' to
#   make it easier to call.
from car_functions import build_car as bc

# Can call the function 'build_car' using the alias given (bc).
car_profile = bc('chevy', 'blazer',
                    drive='four wheel',
                    shape='suv',
                    doors='4')

print(car_profile)

