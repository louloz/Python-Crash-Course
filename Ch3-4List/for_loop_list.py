# Python Crash Course, Eric Matthes, no starch press
# Textbook Exercises

# Louis Lozano
# 3-1-2019
# for_loop_list.py

# Creates a list using list comprehension.
numbers = [num for num in range(1, 1001)]

for num in numbers:
    print(num)

print(numbers)

# min() returns minimum number in a list.
min_number = min(numbers)

# max() returns maximum number in a list.
max_number = max(numbers)

print(min_number)
print(max_number)

# sum() adds all items in a list together and returns the sum.
sum_of_numbers = sum(numbers)

print(sum_of_numbers)
