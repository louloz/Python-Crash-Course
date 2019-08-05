# Python Crash Course, Eric Matthes, no starch press
# Ch8 Functions
# Textbook Exercises

# Louis Lozano
# 3-23-2019
# 8-15_print_models.py

# Description: This program is meant to show how importing in python works.
#   The functions imported are used to print t-shirt designs.

# Let's you use all functions defined in printing_functions.py.
# The 'as' key word let's you make an alias for the module name.
import printing_functions as pf
        
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)
