# Class 04
# Task 02
# A simple program that takes a list of numbers
# and prints out the list where there are numbers that are bigger
# than the number that they go after.

some_list = [2, 56, 34, 12, 40, 100, 55, 16, 4]

new_list = [num for n, num in zip(some_list, some_list[1:]) if num > n]

print(new_list)
