# Python Crash Course, Eric Matthes, no starch press
# Ch6 Dictionaries
# Textbook Exercises

# Louis Lozano
# 3-6-2019
# 6-4_glossary2.py

# Stores  key-value pairs of programming terms and definitions.
glossary = {'string': 'Text data.',
            'int': 'Integer data.',
            'list': 'Stores multiple pieces of data. Can be modified.',
            'tuple': 'Stores multiple pieces of data. Cannot be modified.',
            'if statment': 'Used to test a conditional statement.'}

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
