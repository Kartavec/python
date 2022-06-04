# coding: UTF-8
from functools import reduce


def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result


print([el for el in fact(4)])
