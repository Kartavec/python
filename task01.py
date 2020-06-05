# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys


def get_salary(hours, rate, bonus):
    salary = (hours * rate) + bonus
    return salary


def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None


def print_help():
    message = """
Введены некорректные данные! 
             
Правильный формат ввода:  
python task01.py %HOURS% %RATE% %BONUS%, 
               
Например, 
python task01.py 12 160 50000
"""
    print(message)


def convert_input_to_int(input):
    result = []
    for value in input:
        if convert_to_int(value) is None:
            print_help()
            sys.exit()
        else:
            result.append(convert_to_int(value))
    return result


def check_input_for_quantity(input):
    if len(input) != 3:
        print_help()
        sys.exit()


if __name__ == '__main__':
    values = sys.argv[1:]
    check_input_for_quantity(values)
    converted_values = convert_input_to_int(values)
    hours, rate, bonus = converted_values
    salary = get_salary(hours, rate, bonus)

    result = (f'Количество отработанных часов: {hours}\n'
              f'Ставка в час: {rate}\n'
              f'Бонус: {bonus}\n'
              f'\n'
              f'Заработная плата: {salary}')

    print(result)
