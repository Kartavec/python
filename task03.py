from task02 import convert_to_int


class CustomListElementValueError(Exception):
    pass


if __name__ == '__main__':
    result = []
    while True:
        print()
        user_input = input('Введите значение для добавления в список. Для окончания наберите "STOP". >>')

        if user_input == 'STOP':
            break

        if convert_to_int(user_input) is not False:
            result.append(convert_to_int(user_input))
        else:
            try:
                raise CustomListElementValueError('Неверный ввод! Введите число!')
            except CustomListElementValueError as e:
                print(f'Полученная ошибка: {e}')

    print()
    print('Элементы списка: ')
    for el in result:
        print(el)
