# Class 04
# Task 06
# A simple program that generates 2 scripts:
# the 1st script generates integers starting from the given number,
# the 2nd script iterates the elements of the given list.
# The scripts must must come to a stop at some point defined by the program.

from itertools import count
from itertools import cycle

def iter_func(start_num, end_num):
    for num in count(start_num):
        if num > end_num:
            break
        else:
            print(num)

def cycle_func(some_list, itera):
    num = 0
    iterat = cycle(some_list)
    while num < itera:
        print(next(iterat))
        num += 1

iter_func(1, 10)

some_list = [1, 2, 3]

cycle_func(some_list, 6)



