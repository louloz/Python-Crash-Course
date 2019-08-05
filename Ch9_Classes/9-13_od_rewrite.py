# Python Crash Course, Eric Matthes, no starch press
# Ch6 Dictionaries
# Textbook Exercises

# Louis Lozano
# 04-01-2019
# 9-13_od_rewrite.py

# Python Version: 3.5.3
# Description: Uses a module from the Python Standard Library (collections)
#   and a class (OrderedDict) from that module to create an ordered dictionary.
#   Prints keys, values, and key-value pairs in order they were added, unlike
#   a regular dictionary.

from collections import OrderedDict

glossary = OrderedDict()

glossary['string'] = 'Text data.'
glossary['int'] = 'Integer data.'
glossary['list'] = 'Stores multiple pieces of data. Can be modified.'
glossary['tuple'] = 'Stores multiple pieces of data. Cannot be modified.'
glossary['if statment'] = 'Used to test a conditional statement.'

# Loops through each key-value pair
# item() returns a list of key-value pairs
for term, definition in glossary.items():
    print(term.title() + ": " + definition)

# Loops through each key
# keys() returns a list of keys.
for term in glossary.keys():
    print(term)

# Loops through each value
# values() returns a list of values.
for definition in glossary.values():
    print(definition)
