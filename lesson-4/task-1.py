# coding: UTF-8
from sys import argv
# python lesson-4/task-1.py 2 100 500
try:
    script, hours, bid, award = argv
    print("Result: ", (float(hours) * float(bid)) + float(award))
except TypeError:
    print('Error!')
except ValueError:
    print('Error!')
