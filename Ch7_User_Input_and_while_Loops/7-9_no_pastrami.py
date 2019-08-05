# Python Crash Course, Eric Matthes, no starch press
# Ch7 User Input and while Loops
# Textbook Exercises

# Louis Lozano
# 3-12-2019
# 7-9_no_pastrami.py

# Description: Adds code to 7-8_del.py that takes the same list(sandwich_orders)
#   but with multiple instances of 'pastrami'. Then the program
#   removes each of these instances. 

# Original list with added instances of 'pastrami'.
sandwich_orders = ['turkey', 'pastrami', 'chicken', 'pastrami', 'pastrami',
                   'beef', 'cheese', 'veggie']

finished_sandwiches = []

print('\nThe sandwiches ordered today were: \n')

for sandwich_order in sandwich_orders:
    print('\t' + sandwich_order)

print('\nThe deli has run out of pastrami.\n')

# Removes each instance of 'pastrami' until there are no more.
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()

    print('Your ' + finished_sandwich + ' sandwich is ready.')

    finished_sandwiches.append(finished_sandwich)

print('\nThe sandwiches made today were: \n')

for finished_sandwich in finished_sandwiches:
    print('\t' + finished_sandwich)
