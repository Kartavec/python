# Class 04
# Task 05
# A simple program that generates a list of even numbers
# in the range from 100  to 1000 using the range() function and a list generator
# The output is the product of all numbers from the list
# The program uses the reduce(0 function.

from functools import reduce

some_list = [num for num in range(100, 1001) if num % 2 == 0]

def some_func(prev_num, num):
    return prev_num * num

print(reduce(some_func, some_list))
