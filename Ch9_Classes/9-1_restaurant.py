# Python Crash Course, Eric Matthes, no starch press
# Ch9 Classes

# Louis Lozano
# 3-26-2019
# 9-1_restaurant.py

#Python Version: 3.5.3
# Description: Creates a restaurant class, creates an instance from that class,
#   and calls two methods from the class on that instance. One describes the
#   restaurant and one prints a message stating that it is open.

class Restaurant():
    '''This class models a restaurant.'''

    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize restaurant_name and cuisine_type attributes.'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''Prints a message describing the restaurant.'''
        print('Restaurant Name: ' + self.restaurant_name.title())
        print('Cuisine Type: ' + self.cuisine_type.title())

    def open_restaurant(self):
        '''Prints a message stating the restaurant is open.'''
        print(self.restaurant_name.title() + ' is open!')

my_restaurant = Restaurant("louies' pizza", 'italian')

my_restaurant.describe_restaurant()

my_restaurant.open_restaurant()
