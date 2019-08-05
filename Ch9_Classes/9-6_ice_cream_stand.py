# Python Crash Course, Eric Matthes, no starch press
# Ch9 Classes

# Louis Lozano
# 3-28-2019
# 9-6_ice_cream_stand.py

# Python Version: 3.5.3
# Description: Creates a restaurant class. Creates a ice cream stand which is
#   a child of the restaurant class. Creates an instance of the child class
#   and call a method of the child class.

# Parent Class
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

# Child Class of the Restaurant class.
# Inherits all attributes and methods of the parent.
class IceCreamStand(Restaurant):
    '''This class models an ice cream stand.'''

    def __init__(self, restaurant_name, cuisine_type):
        '''
        Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand.
        '''
        # Calls __init__ method from Restaurant.
        super().__init__(restaurant_name, cuisine_type)
        
        # Attribute specific to IceCreamStand.
        self.flavors = ['blackberry', 'lemon', 'blueberry', 'mango']

    # Method specific to IceCreamStand.
    def get_flavors(self):
        '''Prints ice cream flavors available.'''
        for flavor in self.flavors:
            print(flavor)

ice_cream_stand = IceCreamStand('chillz', 'ice cream')

ice_cream_stand.get_flavors()
