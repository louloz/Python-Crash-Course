# Python Crash Course, Eric Matthes, no starch press
# Textbook Exercises

# Louis Lozano
# 2-26-2019
# list_modify.py

guests = ['susan', 'amy', 'dave']

invite = ", you are invited to dinner!"

print(guests)

print('\n')

print(guests[0].title() + invite)
print(guests[1].title() + invite)
print(guests[2].title() + invite)

cant_message = ", can't make it to dinner."

# pop() removes item from list while letting you use it's data.
lost_guest = guests.pop(0)

print('\n')

print(lost_guest.title() + cant_message)

# insert() puts an item in the list at given index. Moves everything one space to the right.
guests.insert(0, 'tim')

print('\n')

print(guests)

print('\n')

print(guests[0].title() + invite)
print(guests[1].title() + invite)
print(guests[2].title() + invite)

table_message = "We found a bigger table!"

print('\n')

print(table_message)

guests.insert(2, 'steve')

# append() adds an item to the end of a list.
guests.append('mary')

print('\n')

print(guests)

print('\n')

print(guests[0].title() + invite)
print(guests[1].title() + invite)
print(guests[2].title() + invite)
print(guests[3].title() + invite)
print(guests[4].title() + invite)

notable_message = "We can't get the table in time! \nWe only have room for 2 guests. \nYou can't come, "

kicked_guest1 = guests.pop()
kicked_guest2 = guests.pop()
kicked_guest3 = guests.pop()

print("\n")

print(notable_message + kicked_guest1.title() + ".")
print(notable_message + kicked_guest2.title() + ".")
print(notable_message + kicked_guest3.title() + ".")

print("\n")

print(guests)

print("\n")

still_message = ", you're still invited!"

print(guests[0].title() + still_message)
print(guests[1].title() + still_message)

del guests[1]
del guests[0]

print("\n")

print(guests)

# del deletes an item from a list of the given index. Ex. del guest[2]
# remove() looks for given parameter in list and removes it. Ex. guest.remove('tim')
