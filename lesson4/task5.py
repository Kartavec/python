from functools import reduce

def reducer_func(result, multiplier):
    return result * multiplier

generator = (numb for numb in range(100, 1001) if numb % 2 == 0)
print(reduce(reducer_func, generator))
