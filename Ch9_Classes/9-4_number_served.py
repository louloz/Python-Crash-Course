# Python Crash Course, Eric Matthes, no starch press
# Ch9 Classes

# Louis Lozano
# 3-27-2019
# 9-4_numbers_serverd.py

# Python Version: 3.5.3
# Description: Creates a restaurant class, creates an instances from that class.
#   Defines an atrribute (number_served) with a default value. Defines two
#   methods used to modify the sttribute. Modifies the attribute directly and
#   then uses the two methods to modify the attribute. The attribute is printed
#   each time it is modified.

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

# Creates an inwstance of the Restaurant class.
restaurant = Restaurant("crepe castle", 'french')

print(restaurant.number_served)

# Sets attribute directly.
restaurant.number_served = 5

print(restaurant.number_served)

# Sets attribute using a method.
restaurant.set_number_served(7)

print(restaurant.number_served)

# Increments attribute by a number using a method.
restaurant.increment_number_served(78)

print(restaurant.number_served)
