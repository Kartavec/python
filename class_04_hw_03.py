# Class 04
# Task 03
# A simple program that generates a list of numbers in the range from 20 to 240
# The list contains numbers that are multiple of 20 and 21

print([num for num in range(20, 241) if num % 20 == 0 or num % 21 == 0])

