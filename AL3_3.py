import random

SIZE = 10
MIN_ = 0
MAX_  = 100
array = [random.randint(MIN_, MAX_) for _ in range(SIZE)]

m = 0
n = 0
for i in range(SIZE):
    if array[i] < array[m]:
        m = i
    elif array[i] > array[n]:
        n = i
print(f'{array} \nmin: {array[m]} max: {array[n]}')
b = array[m]
array[m] = array[n]
array[n] = b
print(f'Replacement \n{array}')