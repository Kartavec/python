def print_user(*, first_name, last_name, birthday_year, city, email, phone):
    print(f'{first_name} {last_name} {birthday_year} {city} {email} {phone}')


userdata = str(input(
    'Введите данные пользователя через пробел: имя, фамилия, год рождения, город проживания, email, телефон ')).split()

try:
    print_user(
        first_name=userdata[0],
        last_name=userdata[1],
        birthday_year=userdata[2],
        city=userdata[3],
        email=userdata[4],
        phone=userdata[5]
    )
except IndexError:
    print('Ошибка ввода. Видимо вы пропустили что-то')
