# Ch9 Classes

# Louis Lozano
# 4-01-2019
# admin.py

# Python Version: 3.5.3
# Description: A module that holds the classes related to system admins.

# Imports the User class from the user module because the Admin class
#   needs access to it's parent class.
from user import User

class Admin(User):
    '''This class models an Admin.'''

    def __init__(self, first_name, last_name, age, email):
        '''
        Initialize attributes from the parent class.
        Then initialize attributes specific to Admin.
        '''
        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges()

class Privileges():
    '''This class models admin privileges.'''
    def __init__(self):
        '''Initialize attribute.'''
        self.privileges = ['post', 'ban', 'reinstate', 'delete post']

    def show_privileges(self):
        '''Prints a list of admin privileges.'''
        print('Admin Privileges:')
        for privilege in self.privileges:
            print('\t' + privilege.title())
