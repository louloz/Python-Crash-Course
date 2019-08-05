# Python Crash Course, Eric Matthes, no starch press
# Ch5 if statements
# Textbook Exercises

# Louis Lozano
# 3-5-2019
# if_else_elif.py

alien_color = 'green'

# An if statment test a condition. If the condition is true, the indented
# code on the next line is executed. If the condition is false,
# the code is skipped.
if alien_color == 'green':
    print("You earned 5 points!")

if alien_color == 'yellow':
    print("You earned 10 points!")

alien_color = 'yellow'

if alien_color == 'green':
    print("You earned 5 points!")
# An else statment executes code if the if statment it is a part of
# returns false.
else:
    print("You earned 10 points!")

alien_color = 'red'

if alien_color == 'green':
    print("You earned 5 points!")
# An elif statment is an if statment after the first one that test another
# condition.
elif alien_color == 'yellow':
    print("You earned 10 points!")
elif alien_color == 'red':
    print("You earned 15 points!")
