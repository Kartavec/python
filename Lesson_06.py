# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения. #### Например, в первом задании выводим целые числа, начиная с 3.
# # При достижении числа 10 — завершаем цикл. Вторым пунктом необходимо предусмотреть условие,
# # при котором повторение элементов списка прекратится.

from itertools import count

for el in count(3):
    if el == 10:
        break
    print(el)

from itertools import cycle

c = 0
for el in cycle('ABC'):
    if c > 10:
        break
    print(el)
    c += 1

