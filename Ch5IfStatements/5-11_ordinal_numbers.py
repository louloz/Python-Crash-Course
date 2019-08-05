# Python Crash Course, Eric Matthes, no starch press
# Ch5 if statements
# Textbook Exercises

# Louis Lozano
# 3-5-2019
# 5-11_ordinal_numbers.py

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# A for loop that uses conditional statements to handle certain
# items in a list differently.
for number in numbers:
    if number == 1:
        print(str(number) + 'st')
    elif number == 2:
        print(str(number) + 'nd')
    elif number == 3:
        print(str(number) + 'rd')
    else:
        print(str(number) + 'th')
