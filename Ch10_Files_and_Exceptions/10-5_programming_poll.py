# Python Crash Course, Eric Matthes, no starch press
# Ch10 Files and Exceptions
# Textbook Exercises

# Louis Lozano
# 06-21-2019
# 10-5_programming_poll.py

# Python Version: 3.5.3
# Description: Uses a while loop to ask people if they like programming and
#   stores their responses in a file 'programming_poll.txt'.

prompt = 'Why do you like programming?: '

answer = ''

filename = 'programming_poll.txt'

# The 'a' in the open() method indicates the file can be written too and it's
#   contents will not be deleted upon reopening the file. Opens the file in
#   'Append mode'.
with open(filename, 'a') as file_object:
    
    while True:
        answer = input(prompt)

        if answer == 'q' or answer == 'quit' or answer == 'Q' or answer == 'Quit':
            break

        file_object.write(answer + '\n')
