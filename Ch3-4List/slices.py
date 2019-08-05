# Python Crash Course, Eric Matthes, no starch press
# Textbook Exercises

# Louis Lozano
# 3-1-2019
# slices.py

pizzas = ['cheese', 'mushroom', 'basil', 'pepper', 'garlic']

# A for loop stores the first item of list(pizzas) in a variable(pizza) then
# executes code on the next indented lines. After it goes back to first line
# of the loop storing the next item of the list(pizzas) in the variable(pizza)
# and repeats the process until it has gone through all the items in the list.
for pizza in pizzas:
    print("I like " + pizza + " pizza!")

print("Pizza is my favorite food!")

####

animals = ['ducks', 'fish', 'frogs']

for animal in animals:
    print("Lots of " + animal + " live in this lake.")

print("They all like to swim!")

####

# Slices allow you to acces specific parts of a list.

# Slice used to access the first 3 items in a list.
print("The first three items in the list are: " + str(pizzas[:3]))

# Slice used to access the middle 3 items in a list.
print("Three items from the middle of the list are: " + str(pizzas[1:4]))

# Slice used to access the last 3 items in a list.
print("The last three items on the list are: " + str(pizzas[-3:]))

# Slice used to make a copy of a list.
friend_pizzas = pizzas[:]

# append() used to add a different item to the end of each list.
pizzas.append('pineapple')

friend_pizzas.append('pepperoni')

print("My favorite pizzas are: ")

# for loop used to print each item in list.
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are: ")

for pizza in friend_pizzas:
    print(pizza)
