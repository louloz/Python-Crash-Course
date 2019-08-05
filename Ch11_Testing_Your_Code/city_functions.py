# Python Crash Course, Eric Matthes, no starch press
# Ch11 Files and Exceptions
# Textbook Exercises

# Louis Lozano
# 07-07-2019
# Try It Yourself: 11-1 'city_functions.py'

# Python Version: 3.5.3

# Description: Function that gets and formats a city, country, and population.
#   Population is optional.

def city_country(city_name, country_name, population=''):
    
    if population:
        city = city_name.title()
        country = country_name.title()
        city_and_country = city + ', ' + country + ' Population: ' + \
                           str(population)
        
    else:
        city = city_name.title()
        country = country_name.title()
        city_and_country = city + ', ' + country
        
    return city_and_country
