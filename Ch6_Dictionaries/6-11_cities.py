# Python Crash Course, Eric Matthes, no starch press
# Ch6 Dictionaries
# Textbook Exercises

# Louis Lozano
# 3-8-2019
# 6-11_cities.py

# Nesting dictionaries in a dictionary.
cities = {
    'denver' : {'country' : 'usa',
               'population' : '680,000',
               'language' : 'english' },
    'tokyo' : {'country' : 'japan',
              'population' : '9,250,000',
              'language' : 'japanese'},
    'bogota' : {'country' : 'colombia',
               'population' : '10,700,000',
               'language' : 'spanish'}
    }

# Loops through cities dictionary.
for city, info in cities.items():
    print("\n")
    print(city.title()) # Prints key(city name) of cities.
    for k, v in info.items(): # Loops through value(dictionaries) of cities.
        print(k.title() + ": " + v.title()) # Prints contents of nested dictionary.
