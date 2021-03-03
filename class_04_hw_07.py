# Class 04
# Task 07
# A simple program that generates an object generator
# The function should called with this command -
# for el in fibo_gen(n)
# The function generates factorial
# The cycle should show only the first n numbers

from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

gener = fibo_gen()

n = 0
for num in gener:
    if n < 10:
        print(num)
        n += 1
    else:
        break

    
    

        
