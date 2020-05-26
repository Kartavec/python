def get_user_info(name, surname, year_of_birth, town, email, phonenumber):
    result = f'Ваше имя - {surname} {name}, Вы {year_of_birth} года рождения, живете в городе {town}, ' \
             f'адрес электронной почты - {email}, номер телефона - {phonenumber}.'
    return result


if __name__ == '__main__':

    name = input('Введите Ваше имя: ')
    surname = input('Введите Вашу фамилию: ')
    year_of_birth = input('Введите год Вашего рождения: ')
    town = input('Укажите городо проживания: ')
    email = input('Укажите адрес электронной почты: ')
    phonenumber = input('Укажите телефонный номер: ')

    print(get_user_info(
        name=name,
        surname=surname,
        year_of_birth=year_of_birth,
        town=town,
        email=email,
        phonenumber=phonenumber
    ))
