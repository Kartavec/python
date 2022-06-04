# coding: UTF-8
from itertools import cycle


def cycle_loop(list, limit=10):
    for i, v in enumerate(cycle(list)):
        if i > limit:
            break
        yield v


print(list(cycle_loop([1, 2, 3])))
