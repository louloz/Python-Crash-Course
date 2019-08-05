# Python Crash Course, Eric Matthes, no starch press
# Ch5 if statements
# Textbook Exercises

# Louis Lozano
# 3-5-2019
# if_else_elif2.py

age = 28

# An if-elif-else chain is good if you only want one result.
if age < 2:
    print("This person is a baby.")
elif age < 4:
    print("This person is a toddler.")
elif age < 13:
    print("This person is a kid.")
elif age < 20:
    print("This person is a teenager.")
elif age < 65:
    print("This person is an adult.")
else:
    print("This person is an elder.")

favorite_fruits = ['mango', 'pear', 'blackberry']

# A series of if statments are good if you want multiple results.
if 'pear' in favorite_fruits:
    print("You like pears!")
if 'peach' in favorite_fruits:
    print("You like peaches!")
if 'mango' in favorite_fruits:
    print("You like mangoes!")
if 'lemon' in favorite_fruits:
    print("You like lemons!")
if 'blackberry' in favorite_fruits:
    print("You like blackberries!")
