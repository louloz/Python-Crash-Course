# Python Crash Course, Eric Matthes, no starch press
# Ch7 User Input and while Loops
# Textbook Exercises

# Louis Lozano
# 3-9-2019
# 7-4_pizza_toppings.py

prompt = "\nEnter a pizza topping: "
prompt += "\n(Enter 'quit' when you are finished.) "

# A while Loop runs while a given condition is True.
# This while Loop runs until a break statment is executed.
while True:
    topping = input(prompt)

    if topping == 'quit':
        break

    print("\n" + topping.title() + " was added to your pizza.")

# A while Loop makes it possible for the user to choose when the program ends.
