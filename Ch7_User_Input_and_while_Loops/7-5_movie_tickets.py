# Python Crash Course, Eric Matthes, no starch press
# Ch7 User Input and while Loops
# Textbook Exercises

# Louis Lozano
# 3-9-2019
# 7-5_movie_tickets.py

prompt = "\nEnter your age: "
prompt += "\n(Enter 'quit' when you are finished.) "

active = True

# A while Loop runs while a given condition is True.
# This while Loop runs until active is equal to false.
while active:
    age = input(prompt)

    if age == 'quit':
        active = False
        continue # Skips the rest of the code inside loop without exiting.

    age = int(age) # Converts user input to int type for comparisons. 
    if age < 3:
        print("Your ticket will be free.")
    elif age < 13:
        print("Your ticket will be $10.")
    else:
        print("Your ticket will be $15.")
