# Python Crash Course, Eric Matthes, no starch press
# Ch7 User Input and while Loops
# Textbook Exercises

# Louis Lozano
# 3-8-2019
# 7-3_multiples_of_ten.py

# Description: Lets the user enter a number and
# finds out if it is a multiple of 10.

number = input("Please enter a number: ")

number = int(number)

# The modulo operator(%) divides one number by another
# and returns the remainder.
if number % 10 == 0:
    print("This number is a multiple of 10.")
else:
    print("This number is not a multiple of 10.")
