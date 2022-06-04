# coding: UTF-8
from functools import reduce
print(reduce(lambda x, y: x*y, [i for i in range(100, 1001) if i % 2 == 0]))
