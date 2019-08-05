# Python Crash Course, Eric Matthes, no starch press
# Ch7 User Input and while Loops
# Textbook Exercises

# Louis Lozano
# 3-8-2019
# 7-1_rental_car.py

# Prompts user for input and stores input as a string value in variable.
car = input("What kind of rental car would you like?")

if car == 'bmw':
    print("Lets see if I can find you a " + car.upper() + ".")
else:
    print("Lets see if I can find you a " + car.title() + ".")
