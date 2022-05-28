# coding=utf-8
def int_input(prompt):
    value = None
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print('Ошибка ввода')
            continue
        break
    return value


my_list = [7, 5, 3, 3, 2]
new_rate = int_input('Введите новый элемент рейтинга: ')
my_list.append(new_rate)
my_list.sort(reverse=True)
print('Рейтинг: ', my_list)
