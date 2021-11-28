# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.

users = []


def save_user(name, surname, birth_year, city, email, phone_numb):
    users.append((name, surname, birth_year, city, email, phone_numb))


def show_users():
    if len(users) == 0:
        print('Список пуст\n')
    for user in users:
        print(*user)


while True:
    choice = int(input('\n1. Ввеcти инфорамацию о пользователе\n2. Вывести информацию о пользователях\n3. Выход\n'))
    if choice == 1:
        name = input('Введите имя: ')
        surname = input('Введите фамилию: ')
        birth_year = int(input('Введите год рождения: '))
        city = input('Введите город проживания: ')
        email = input('Введите email: ')
        phone_numb = input('Введите номер телефона: ')

        save_user(name=name, surname=surname, birth_year=birth_year, city=city, email=email, phone_numb=phone_numb)
    elif choice == 2:
        print()
        show_users()
    else:
        break



