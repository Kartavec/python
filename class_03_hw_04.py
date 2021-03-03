# Class 03
# Task 04
# A simple function that takes 2 positional args:
# a positive integer and a negative integer.
# It returns the first integer to the power of the second integer.

# Solution 1

def my_func(x, y):
    return x ** y

print(my_func(2, -7))

# Solution 2
# A simple function that takes 2 positional args:
# a positive integer and a negative integer
# It returns the first integer to the power of the second integer.

def my_func_02(x, y):
    if y < 0:
        y = abs(y)
    result = 1
    while y:
        result *= 1/x
        y -= 1
        
    return result

print(my_func_02(2, -5))
