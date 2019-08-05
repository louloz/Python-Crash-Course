# Python Crash Course, Eric Matthes, no starch press
# Textbook Exercises

# Louis Lozano
# 3-1-2019
# for_loop_list_2.py

# List comprehension used to create a list of odd numbers between 1 and 20
odd_numbers = [odd for odd in range(1, 20, 2)]

for num in odd_numbers:
    print(num)

# List comprehension used to create a list of multiples of 3 from 3 to 30.
multiples_of_three = [num*3 for num in range(3, 30)]

for three in multiples_of_three:
    print(three)

# List comprehension used to create a list of cubes from 1 to 10.
cubes = [num**3 for num in range(1, 11)]

for cube in cubes:
     print(cube)
