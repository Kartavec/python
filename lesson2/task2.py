arr = list(input(f'Введите элементы массива через запятую:  ').split(','))
i = 0
while i < len(arr)-1:
    to_swap = arr[i]
    arr[i] = arr[i+1]
    arr[i+1] = to_swap
    i+=2
print(arr)

