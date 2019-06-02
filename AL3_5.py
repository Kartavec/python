import random

SIZE = 10
MIN_ = -100
MAX_  = 100
array = [random.randint(MIN_, MAX_) for _ in range(SIZE)]

print(array)

i = 0
index = -1
while i < SIZE:
    if array[i] < 0 and index == -1:
        index = i
    elif array[i] < 0 and array[i] > array[index]:
        index = i
    i += 1

print(f'Аrray position {index} : maximum negative element {array[index]}')