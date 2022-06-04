# coding: UTF-8
def unique(some_list):
    for i in range(len(some_list)):
        if some_list[i] not in (some_list[:i] + some_list[i + 1:]):
            yield some_list[i]


arr = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(list(unique(arr)))
