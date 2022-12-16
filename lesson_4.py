"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
 Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для
 конкретных значений необходимо запускать скрипт с параметрами.
 """

from functools import partial

def salary_amount(q_hours, hour_rate, bonus_amount):
    salary = q_hours * hour_rate + bonus_amount
    print(salary)


salary_amount(40, 300, 5000)

new_salary = partial(salary_amount, 40, 300)
print(new_salary(5000))

"""2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше 
предыдущего элемента.
"""

from random import randint
random_list = [randint(0, 100) for i in range(10)]
new_list = []
new_list = [random_list[i] for i in range(1, len(random_list)) if random_list[i] > random_list[(i-1)]]
print(random_list)
print(new_list)


"""3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
"""

list_20_to_240 = []
list_20_to_240 = [i for i in range(20, 240) if i % (20) == 0 or i % (21) == 0]
print(list_20_to_240)

"""4. Представлен список чисел. Определите элементы списка, не имеющие повторений. Сформируйте итоговый 
массив чисел, соответствующих требованию. Элементы выведите в порядке их следования в исходном списке. 
Для выполнения задания обязательно используйте генератор.
"""

random_list_1 = [randint(0, 10) for i in range(10)]   #генерирую список из случайных чисел
print(random_list_1)
list_without_repeat= []
list_without_repeat = [i for i in random_list_1 if random_list_1.count(i) == 1]
print(list_without_repeat)



"""5. Реализовать формирование списка, используя функцию range() и возможности генератора. 
В список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить результат 
вычисления произведения всех элементов списка.
"""

from functools import reduce
def multiply(pre_el, el):
    return pre_el * el

list_for_multiply = []
list_for_multiply = [el for el in range(100, 1001) if el % 2 == 0]
print(list_for_multiply)

print(reduce(multiply, list_for_multiply))


"""6. Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее.
"""

from itertools import cycle
from itertools import count

for i in count(8, 2):
    if i > 16:
        break
    else:
        print(i)



counter = 0
for it in cycle('random'):
    if counter > 8:
        break
    print(it)
    counter += 1


"""7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом: 
for el in fact(n). Она отвечает за получение факториала числа. В цикле нужно выводить только первые 
n чисел, начиная с 1! и до n!.
"""

from math import factorial

def fact(n):
    for i in range(n):
        yield (factorial(i))


factorial_generator = fact(11)
print(factorial_generator)

for i in factorial_generator:
    print(i)