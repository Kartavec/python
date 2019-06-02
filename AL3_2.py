import random
SIZE = 10
array = [0]*SIZE
even = []
for i in range(SIZE):
    array[i] = int(random.random() * 10) + 10
    if array[i] % 2 == 0:
        even.append(i)
print(array)
print('Index of even elements: ', even)


