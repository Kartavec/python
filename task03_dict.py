def convert_to_int(input_string):
    try:
        return int(input_string)
    except ValueError:
        pass


def get_month_name(number):
    months = {1: 'Январь',
              2: 'Февраль',
              3: 'Март',
              4: 'Апрель',
              5: 'Май',
              6: 'Июнь',
              7: 'Июль',
              8: 'Август',
              9: 'Сентябрь',
              10: 'Октябрь',
              11: 'Ноябрь',
              12: 'Декабрь'}
    return months[number]


if __name__ == '__main__':
    while True:
        month_number = convert_to_int(input('Введите номер месяца (1-12):'))
        if month_number in range(1, 13):
            month_name = get_month_name(month_number)
            print(f'Месяц под номером {month_number} называет {month_name.lower()}.')
            break
        else:
            print('Некорректный ввод, попробуйте еще раз.')
