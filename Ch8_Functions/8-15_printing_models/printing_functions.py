# Python Crash Course, Eric Matthes, no starch press
# Ch8 Functions
# Textbook Exercises

# Louis Lozano
# 3-23-2019
# 8-15_printing_functions.py

# Description: This file contains two function definitions for printing
#   t-shirt designs. They can be used in another python file that lies
#   in the same directory by importing this file into it with the
#   'import' keyword.

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until there are none left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
    
        # Simulate creating a 3d print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
