# coding: UTF-8
from itertools import count


def nums(start_from, limit=50):
    for i, v in enumerate(count(start_from)):
        if i > 50:
            break
        yield v


print(list(nums(10)))
