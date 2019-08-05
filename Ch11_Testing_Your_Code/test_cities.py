# Python Crash Course, Eric Matthes, no starch press
# Ch11 Files and Exceptions
# Textbook Exercises

# Louis Lozano
# 07-07-2019
# Try It Yourself: 11-1 'test_cities.py'

# Python Version: 3.5.3

# Description: Test city_country function for 2 and three parameters given.

# Module used for testing
import unittest

# Imports function being tested
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    '''Test for '11-1_city_functions.py' .'''
    
    def test_city_country(self):
        '''Do cities like Santiago, Chile work?'''
        formatted_city = city_country('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_country_population(self):
        '''Do cities like Santiago, Chile 500000 work?'''
        formatted_city = city_country('santiago', 'chile', 500000)
        self.assertEqual(formatted_city, 'Santiago, Chile Population: 500000')

# Runs all test
unittest.main()
