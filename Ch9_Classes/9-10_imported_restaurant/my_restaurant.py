# Python Crash Course, Eric Matthes, no starch press
# Ch9 Classes

# Louis Lozano
# 4-01-2019
# my_restaurant.py

# Python Version: 3.5.3
# Description: Imports the Restaurant class from the restaurant module. Creates
#   an instance of that class. Call methods from that class to confirm the
#   import is working properly.

from restaurant import Restaurant

my_restaurant = Restaurant("louies' pizza", 'italian')

my_restaurant.describe_restaurant()

my_restaurant.open_restaurant()
