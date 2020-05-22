def convert_to_int(input_string):
    try:
        return int(input_string)
    except ValueError:
        pass


def get_month_name(number):
    months = ['Январь',
              'Февраль',
              'Март',
              'Апрель',
              'Май',
              'Июнь',
              'Июль',
              'Август',
              'Сентябрь',
              'Октябрь',
              'Ноябрь',
              'Декабрь']
    return months[number-1]


if __name__ == '__main__':
    while True:
        month_number = convert_to_int(input('Введите номер месяца (1-12):'))
        if month_number in range(1, 13):
            month_name = get_month_name(month_number)
            print(f'Месяц под номером {month_number} называет {month_name.lower()}.')
            break
        else:
            print('Некорректный ввод, попробуйте еще раз.')
