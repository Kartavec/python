# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
import random

init_ls = [random.randrange(0, 100) for _ in range(0, 10)]
print(f'Исходный список: {init_ls}')
res_ls = [init_ls[i] for i in range(1, len(init_ls)) if init_ls[i-1] < init_ls[i]]
print(f'Результирующий список: {res_ls}')
