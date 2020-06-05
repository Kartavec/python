# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

import itertools


def repeat_list(input_list, number_of_repetitions):
    count = 0
    for i in itertools.cycle(input_list):
        if count == number_of_repetitions:
            break
        print(i)
        count += 1


if __name__ == '__main__':
    sequence = ['nanananana-nanana-nanana-nanana-nananaaa',
                'nanananana-nanana-nanana',
                'nanananana-olololololooooooooooooooo',
                'lolooooooooooo',
                'lalala-la-lala',
                'lololololoooo-lololo-lololo-lo-lolo']
    number_of_reps = 500
    print(f'Пример работы итератора, выводящего в цикле строки песни Эдуарда Хиля {number_of_reps} раз:')
    repeat_list(sequence, number_of_reps)
