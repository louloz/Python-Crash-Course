# Python Crash Course, Eric Matthes, no starch press
# Ch9 Classes

# Louis Lozano
# 4-01-2019
# restaurant.py

# Python Version: 3.5.3
# Description: A module that holds the Restaurant class.

class Restaurant():
    '''This class models a restaurant.'''

    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize restaurant_name and cuisine_type attributes.'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''Prints a message describing the restaurant.'''
        print('Restaurant Name: ' + self.restaurant_name.title())
        print('Cuisine Type: ' + self.cuisine_type.title())

    def open_restaurant(self):
        '''Prints a message stating the restaurant is open.'''
        print(self.restaurant_name.title() + ' is open!')

    def set_number_served(self, number_served):
        '''Allows you to set the restaurants' number_served.'''
        self.number_served = number_served

    def increment_number_served(self, increment):
        '''Allows you to set the restaurants' number_served.'''
        self.number_served += increment
