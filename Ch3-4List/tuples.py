# Python Crash Course, Eric Matthes, no starch press
# Textbook Exercises

# Louis Lozano
# 3-1-2019
# tuples.py

# A tuple is a list that cannot be modified. If the program
# attempts to modify a tuple, it will cause an error.

# Defines a tuple. 
foods = ('carrots', 'potatoes', 'chicken', 'broccoli', 'garlic')

for food in foods:
    print(food)

# The following line causes an error.
# foods[2] = 'peas'

#### Traceback (most recent call last):
####   File "C:/Users/Louie/Documents/WinPython-64bit-3.5.3.1Qt5/notebooks/PythonCrashCourse/Part1_Basics/Ch3-4List/tuples.py", line 17, in <module>
####     foods[2] = 'peas'
#### TypeError: 'tuple' object does not support item assignment

# A tuple can be redefined.
foods = ('mushrooms', 'potatoes', 'fish', 'broccoli', 'garlic')

for food in foods:
    print(food)
