# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
# быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также
# необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

# а) итератор, генерирующий целые числа, начиная с указанного
from itertools import count, cycle

start = 100
end = 150
ls = []
for i in count(start):
    ls.append(i)
    if i == end:
        break
print(*ls)

# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
start = 1
end = 10
ls.clear()
for i in cycle([i for i in range(start, end, 2)]):
    ls.append(i)
    if end == 0:
        break
    end -= 1
print(*ls)
