# Python Crash Course, Eric Matthes, no starch press
# Ch5 Textbook Exercises

# Louis Lozano
# 3-2-2019
# conditional_test.py

# '=' assigns a value.
veggie = 'Mushroom'

# '==' test for equality.
print(veggie == 'Mushroom')
print(veggie == 'Apple')
print(veggie.lower() == 'mushroom')

# Other conditional operators
print('\n')
print(42 < 21)
print(12 >= 11)

# And statements returns True if both conditions are met.
print(7 <= 7 and 4 == (20 / 5))

# Or statements return True if either condition is met.
print(80 < 40 or 2 > 1)
print(80 < 40 or 2 < 1)

names = ['jon', 'ashley', 'tim']

# Checks if given item is in given list.
# Returns true if it is and false if it is not.
# Assigns the boolean value to a variable.
ashley = 'ashley' in names

david = 'david' in names

print('\n')
print(ashley)
print(david)
