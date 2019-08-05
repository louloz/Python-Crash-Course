# Python Crash Course, Eric Matthes, no starch press
# Ch8 Functions
# Textbook Exercises

# Louis Lozano
# 3-23-2019
# cars_functions.py

# Description: A function that accepts any amount of key-value pairs
#   and creates a dictionary with information about a car.

def build_car(manufacturer, model, **car_specs):
    '''Takes a car manufacturer, model, and any amout of key-value pairs.
    Stores car info given in a dictionary. Returns the dictionary.'''
    specs = {}
    specs['manufacturer'] = manufacturer
    specs['model'] = model

    for key, value in car_specs.items():
        specs[key] = value

    return specs
