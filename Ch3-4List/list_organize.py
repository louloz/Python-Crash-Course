# Python Crash Course, Eric Matthes, no starch press
# Textbook Exercises

# Louis Lozano
# 3-1-2019
# list_organize.py

places = ['Japan', 'China', 'Norway', 'Canada', 'Cartagena' ]

print(places)

# sorted() returns an alphabetically sorted list
# without changing the order of the original list.
print(sorted(places))

print(places)

# Prints list in reverse alphabetical order.
print(sorted(places, reverse=True))

print(places)

# reverse() perminently reverses the order of a list.
places.reverse()

print(places)

places.reverse()

print(places)

#sort() perminently sorts a list into alphabetical order.
places.sort()

print(places)

# Reverse alphabetical order.
places.sort(reverse=True)

print(places)

# len() returns length of a list.
num_places = len(places)

message = "There are " + str(num_places) + " places to go."

print(message)
