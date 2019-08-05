# Python Crash Course, Eric Matthes, no starch press
# Textbook Exercises

# Louis Lozano
# 3-1-2019
# for_loop.py

pizzas = ['cheese', 'mushroom', 'basil']

# A for loop stores the first item of list(pizzas) in a variable(pizza) then
# executes code on the next indented lines. After it goes back to first line
# of the loop storing the next item of the list(pizzas) in the variable(pizza)
# and repeats the process until it has gone through all the items in the list.
for pizza in pizzas:
    print("I like " + pizza + " pizza!")

print("Pizza is my favorite food!")

animals = ['ducks', 'fish', 'frogs']

for animal in animals:
    print("Lots of " + animal + " live in this lake.")

print("They all like to swim!")
