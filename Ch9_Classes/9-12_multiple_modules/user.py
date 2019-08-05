# Python Crash Course, Eric Matthes, no starch press
# Ch9 Classes

# Louis Lozano
# 4-01-2019
# user.py

# Python Version: 3.5.3
# Description: A module that holds the classes related to system users.

class User():
    '''This class models user accounts.'''
    
    def __init__(self, first_name, last_name, age, email):
        '''Initializes attributes.'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        '''Prints information about the user.'''
        print('First Name: ' + self.first_name.title())
        print('Last Name: ' + self.last_name.title())
        print('Age: ' + str(self.age))
        print('Email: ' + self.email)

    def greet_user(self):
        '''Prints a greeting to the user.'''
        print('Hello ' + self.first_name.title() + ' ' +
              self.last_name.title() + '!')

    def increment_login_attempts(self):
        '''Increments login_attempts by 1.'''
        self.login_attempts += 1

    def reset_login_attempts(self):
        '''Resets login_attempts to 0.'''
        self.login_attempts = 0
