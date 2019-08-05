# Python Crash Course, Eric Matthes, no starch press
# Ch9 Classes

# Louis Lozano
# 3-26-2019
# 9-3_users.py

# Python Version: 3.5.3
# Description: 

class User():

    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print('First Name: ' + self.first_name.title())
        print('Last Name: ' + self.last_name.title())
        print('Age: ' + str(self.age))
        print('Email: ' + self.email)

    def greet_user(self):
        print('Hello ' + self.first_name.title() + ' ' +
              self.last_name.title() + '!')

me = User('louie', 'lozano', 28, 'blahblah@maily.com')

so = User('lydia', 'pscholka', 23, 'meowmeow@maily.com')

dude = User('kyle', 'hampster', 19, 'gerbal@maily.com')

me.describe_user()

me.greet_user()

so.describe_user()

so.greet_user()

dude.describe_user()

dude.greet_user()
