# Python Crash Course, Eric Matthes, no starch press
# Ch7 User Input and while Loops
# Textbook Exercises

# Louis Lozano
# 3-8-2019
# 7-2_restaurant_seating.py

group_num = input("How many people are in your dinner group?")

# Converts user input(string value) into an int data type.
# Lets you use user input for numerical comparisons.
group_num = int(group_num)

if group_num > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")
