# Python Crash Course, Eric Matthes, no starch press
# Ch10 Files and Exceptions
# Textbook Exercises

# Louis Lozano
# 06-21-2019
# 10-4_guestbook.py

# Python Version: 3.5.3
# Description: Uses a while loop to prompt for users name, give them a greeting,
#   and record each interaction on a new line in a file 'guest_book.txt'.

flag = True

filename = 'guest_book.txt'

prompt = 'What is your name?: '

guest_name = ''

greeting = ''

# The file closes when the while loop ends.
with open(filename, 'w') as file_object:
    
    while True:
        guest_name = input(prompt)

        # Means to exit the loop.
        if guest_name == 'q' or guest_name == 'quit':
            break
    
        greeting = 'Hello ' + guest_name + '!'
    
        print(greeting)

        # Writes interaction between user and program to the file.
        file_object.write(prompt + guest_name + ' ' + greeting + '\n')
    
