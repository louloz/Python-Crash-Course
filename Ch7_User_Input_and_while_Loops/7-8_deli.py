# Python Crash Course, Eric Matthes, no starch press
# Ch7 User Input and while Loops
# Textbook Exercises

# Louis Lozano
# 3-12-2019
# 7-8_deli.py

# Description: Moves each item from one list of sandwiches to another
#   using a while loop. Prints each item as it is moved and prints the
#   contents of the filled list in order.

sandwich_orders = ['turkey', 'chicken', 'beef', 'cheese', 'veggie']

# Empty list where items in first list will be moved
finished_sandwiches = []

# Removes each item in sandwich_orders and moves them to finished_sandwiches
#   one by one.
while sandwich_orders:
    # pop() removes and returns the last item in the list.
    finished_sandwich = sandwich_orders.pop()

    print('Your ' + finished_sandwich + ' sandwich is ready.')

    finished_sandwiches.append(finished_sandwich)

print('\nThe sandwiches made today were: \n')

# Prints contents of new finished_sandwiches.
for finished_sandwich in finished_sandwiches:
    print('\t' + finished_sandwich)
