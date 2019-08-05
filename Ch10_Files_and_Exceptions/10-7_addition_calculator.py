# Python Crash Course, Eric Matthes, no starch press
# Ch10 Files and Exceptions
# Textbook Exercises

# Louis Lozano
# 06-26-2019
# 10-7_addition_calculator.py

# Python Version: 3.5.3

# Description: Prompts user to enter two number and then adds them and prints
#   the sum to the user. Uses try-except blocks to print a message to the
#   user in case they enter something other then a number. the try-except
#   blocks are used to handle errors and prevent the program from crashing.
#   Uses a while loop to let the user try again in case they enter text
#   instead of a number.

while True:
    try:
        first_num = int(input('Enter a number: '))

    except ValueError:
        print('Invalid Input')
        continue

    else:
        
        try:
            second_num = int(input('Enter another number: '))

        except ValueError:
            print('Invalid Input')
            continue

        else:
            num_sum = first_num + second_num

            response = 'The sum of ' + str(first_num) + ' and ' + str(second_num) \
                       + ' is ' + str(num_sum) + '.'

            print(response)
            break
