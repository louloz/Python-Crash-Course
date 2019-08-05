# Python Crash Course, Eric Matthes, no starch press
# Ch11 Files and Exceptions
# Textbook Exercises

# Louis Lozano
# 07-08-2019
# Try It Yourself: 11-3 'test_Employee.py'

# Python Version: 3.5.3

# Description: Test the Employee class.

import unittest

from Employee import Employee

class TestEmployee(unittest.TestCase):
    '''Test for the class Employee.'''

    def setUp(self):
        '''
        Create an employee for test methods.
        '''

        self.test_hire = Employee('Kirby', 'Popstar', 10000)

    def test_default_raise(self):
        '''Test that default raises are given properly.'''
        self.test_hire.give_raise()
        self.assertEqual(self.test_hire.salary, 15000)

    def test_custom_raise(self):
        '''Test that custom raises are given properly.'''
        self.test_hire.give_raise(70)
        self.assertEqual(self.test_hire.salary, 10070)

# Runs all test.
unittest.main()
