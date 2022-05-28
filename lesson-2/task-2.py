# coding=utf-8
arr = list(input('Введите произвольную строку: '))
print(arr)
arr[:-1:2], arr[1::2] = arr[1::2], arr[:-1:2]
print(arr)
