# Python Crash Course, Eric Matthes, no starch press
# Ch8 Functions
# Textbook Exercises

# Louis Lozano
# 3-22-2019
# 8-14_cars.py

# Description: A function that accepts any amount of key-value pairs
#   and creates a dictionary with information about a car.
#   The function is called to create a car profile.

def build_car(manufacturer, model, **car_specs):
    specs = {}
    specs['manufacturer'] = manufacturer
    specs['model'] = model

    for key, value in car_specs.items():
        specs[key] = value

    return specs

car_profile = build_car('chevy', 'blazer',
                        drive='four wheel',
                        shape='suv',
                        doors='4')

print(car_profile)
