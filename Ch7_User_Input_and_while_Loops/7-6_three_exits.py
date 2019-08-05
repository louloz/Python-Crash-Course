# Python Crash Course, Eric Matthes, no starch press
# Ch7 User Input and while Loops
# Textbook Exercises

# Louis Lozano
# 3-9-2019
# 7-6_three_exits.py

prompt = "\nEnter a pizza topping: "
prompt += "\n(Enter 'quit' when you are finished.) "

# Keeps track of number of toppings for while loop.
topping_num = 0

# This while Loop uses a conditional statement to run and exit.
while topping_num < 5:

    if topping_num == 1:
        print("You have " + str(topping_num) + " topping on your pizza.")
    else:
        print("You have " + str(topping_num) + " toppings on your pizza.")
        
    print("You can fit up to 5.")
    
    topping = input(prompt)

    if topping == 'quit':
        break

    print("\nAdded " + topping.title() + " to your pizza.")

    # Incriments topping_num by one after the user enters a topping.
    topping_num += 1

    if topping_num >= 5:
        print("We cannot fit anymore toppings on your pizza.")
