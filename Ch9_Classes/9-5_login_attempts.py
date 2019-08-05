# Python Crash Course, Eric Matthes, no starch press
# Ch9 Classes

# Louis Lozano
# 3-26-2019
# 9-5_login_attempts.py

# Python Version: 3.5.3
# Description: Creates a User class. Creates and instance from the User class.
#   Increments attribute login_attempts of that instance and resets
#   login_attempts back to 0 using class methods. Prints value of
#   login_attempts attribute after incrementing and reseting.

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

# Creates an instance from the User class.
cat = User('squeaky', 'pscholka', 4, 'gimmiefood@maily.com')

# Prints attribut login_attempts
print(cat.login_attempts)

# Uses a method serveral times to increment login_attempts (by 1 each call).
cat.increment_login_attempts()
cat.increment_login_attempts()
cat.increment_login_attempts()

# Prints login_attempt after incrementing.
print(cat.login_attempts)

# Uses a method to reset login_attempts to 0.
cat.reset_login_attempts()

# Prints login_attempts after reseting it to 0.
print(cat.login_attempts)
