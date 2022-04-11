from functools import reduce

a = reduce(lambda x, y: x * y, [x for x in range(100, 1001) if x % 2 == 0])
print(a)
