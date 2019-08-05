# Python Crash Course, Eric Matthes, no starch press
# Ch11 Files and Exceptions
# Textbook Exercises

# Louis Lozano
# 07-08-2019
# Try It Yourself: 11-3 'Employee.py'

# Python Version: 3.5.3

# Description: Creates an Employee class that takes a first name, last name,
#   and salary. Has a function to give raises.

class Employee():
    '''Models an employee.'''

    def __init__(self, first_name, last_name, salary):
        '''Initializes attribute.'''
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount=5000):
        '''Adds money to an employees salary.'''
        self.salary = self.salary + amount

hire = Employee('Louie', 'Lozano', 50000)

'''
print(hire.salary)

hire.give_raise()

print(hire.salary)

hire.give_raise(100700)

print(hire.salary)
'''
