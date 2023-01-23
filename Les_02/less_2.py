# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

work_list = []
work_len = int(input('Введите длину списка: '))
for i in range(0, work_len):
    work_list.append(input('Введите элемент списка: '))
print(work_list)
for i in range(0, len(work_list)-1, 2):
    work_list[i], work_list[i+1] = work_list[i+1], work_list[i]
print(work_list)