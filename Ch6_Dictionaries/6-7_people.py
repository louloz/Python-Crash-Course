# Python Crash Course, Eric Matthes, no starch press
# Ch6 Dictionaries
# Textbook Exercises

# Louis Lozano
# 3-8-2019
# 6-7_people.py

# Defines a dictionary storing different information about a person
# using key-value pairs.

person1 = {'first name': 'ash',
          'last name': 'ketchum',
          'age': 26,
          'town': 'pallet'}

person2 = {'first name': 'brock',
          'last name': '???',
          'age': 28,
          'town': 'pallet'}

person3 = {'first name': 'misty',
          'last name': '???',
          'age': 24,
          'town': 'pallet'}

# Nesting dictionaries into a list.
people = [person1, person2, person3]

# Loops through list of dictionaries
for person in people:
    for item, info in person.items(): # Loopes through each dictionary
        print(item.title() + ": " + str(info)) # prints dictionary contents
