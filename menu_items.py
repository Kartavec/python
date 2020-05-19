from actions import calculate_days, calculate_time, get_max_digit, get_digits_sum, get_profit, get_profit_by_people
from tools import convert_to_int


def menu_item_1():
    print('Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько '
          'чисел и строк и сохраните в переменные, выведите на экран.')
    name = input('Введите Ваше имя: ')
    age = convert_to_int(input('Введите Ваш возраст: '))
    color = input('Введите Ваш любимый цвет: ')
    print()
    print(f'Вас зовут {name}. Вам возраст - {age}. Ваш любимый цвет - {color}')
    print()


def menu_item_2():
    print('Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате '
          'чч:мм:сс. Используйте форматирование строк.')

    seconds = convert_to_int(input('Введите количество секунд: '))
    format_time = calculate_time(seconds)
    print()
    print(f'Время в формате чч:мм:сс - {format_time}')
    print()


def menu_item_3():
    print('Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.'
          ' Считаем 3 + 33 + 333 = 369.')

    digit = convert_to_int(input('Введите число: '))
    result = get_digits_sum(digit)
    print()
    print(f'Результат - {result}')
    print()


def menu_item_4():
    print('Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. '
          'Для решения используйте цикл while и арифметические операции.')

    number = convert_to_int(input('Введите число: '))
    max_digit = get_max_digit(str(number))
    print()
    print(f'Большая цифра в числе - {max_digit}')
    print()


def menu_item_5():
    print('Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом '
          'работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите '
          'соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки '
          '(соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль '
          'фирмы в расчете на одного сотрудника.')

    revenue = convert_to_int(input('Укажите выручку вашей организации: '))
    costs = convert_to_int(input('Укажите издержки вашей организации: '))

    if costs >= revenue:
        print('Фирма отработала без прибыли')
    else:
        profit = get_profit(revenue, costs)
        print(f'Фирма отработала с прибылью. Рентабельность выручки - {profit}')
        print()
        number_of_people = convert_to_int(input('Укажите количество людей в вашей организации: '))
        profit_by_people = get_profit_by_people(revenue, costs, number_of_people)
        print()
        print(f'Прибыль на человека - {profit_by_people}')
    print()


def menu_item_6():
    print('Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день '
          'спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который '
          'общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров '
          'a и b и выводить одно натуральное число — номер дня.')
    first_result = convert_to_int(input('Укажите результат первого дня: '))
    target_result = convert_to_int(input('Укажите целевой результат: '))
    result_day = calculate_days(first_result, target_result)
    print()
    print(f'Спорсмен достигнет показателя {target_result} км на {result_day} день.')
    print()
