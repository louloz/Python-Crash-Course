# Python Crash Course, Eric Matthes, no starch press
# Ch7 User Input and while Loops
# Textbook Exercises

# Louis Lozano
# 3-12-2019
# 7-10_dream_vacation.py

# Description: Polls users about their dream vacation.
#   Prints the results of the poll.

# Empty dictionary to store persons name(key) and place(value).
responses = {}

# Flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for persons name and response.
    name = input("What is your name?")
    response = input('''If you could go anywhere in the world,
                     where would you go?''')

    # Stores name and response in dictionary.
    responses[name] = response

    # Checks if user wants to continue or end poll.
    repeat = input('Would you like to let another person respond? (yes/no)')

    # Loop ends if user enters no.
    if repeat == 'no':
        polling_active = False

# Polling is complete. Shows the results.
print('\n---Poll Results---')

for name, response in responses.items():
    print(name.title() + " would like to go to " + response.title() + '.')
