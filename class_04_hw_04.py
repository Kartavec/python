# Class 04
# Task 04
# A simple program that takes a list of numbers and generates a new list
# with the same numbers that are not repeated and go in initial order.

some_list = [34, 34, 45, 55, 55, 12, 13, 100, 101, 101]

new_list = [num for num in some_list if some_list.count(num) == 1]

print(new_list)
