# Python Crash Course, Eric Matthes, no starch press
# Ch8 Functions
# Textbook Exercises

# Louis Lozano
# 3-20-2019
# 8-11_unchanged_magicians.py

# Description: This program uses a function to take a list of magicians
#   and print their names one by one. Then it uses another function to
#   add 'the Great' to each name in a copy of the list. The original
#   list is printed to show it's unchanged. The copy is printed to show
#   it stored a modified version of the original list.

# Defines a function that takes a list of magician names and prints each
#   one in order.    
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

# Defines a function that takes the list of magician and adds ' the Great'
#   to their name.
def make_great(magicians):
    # Empty list to hold great magicians
    great_magicians = []

    # while loop to add ' the Great' to each magicians name while moving
    #   them to a new list
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # 'magicians = great_magicians' does not work.

    # Puts each magician back into the original list.
    for great_magician in great_magicians:
        magicians.append(great_magician)

    # Returns list so it can be stored in another list.
    return magicians

# Defines a list of magicians.
magicians = ['David', 'Chris', 'Penn', 'Teller', 'Strange']

# Calls function with the list of magicians.
show_magicians(magicians)

# Makes a copy of the original magician list, makes each magician in the copy
#   great, and stores the modified copy in a new list.
great_magicians = make_great(magicians[:])

print('\n')
# Calls function with the unchanged original list of magicians.
show_magicians(magicians)

print('\n')
# Calls function with the new list of great magicians.
show_magicians(great_magicians)
