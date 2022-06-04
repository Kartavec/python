# coding: UTF-8
# import random


def greater_next(some_list):
    for i in range(1, len(some_list)):
        if some_list[i] > some_list[i-1]:
            yield some_list[i]


# LIST_LENGTH = random.randint(10, 30)
# li = random.sample(range(1, 100), LIST_LENGTH)
# print(f'List length: {LIST_LENGTH}')
# print(f'List: {li}')
li = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print('Result list', end=' ')
print(list(greater_next(li)))

