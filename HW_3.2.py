def user_info():
    name = input('What is your name ')
    last_name = input('What is your last name ')
    date_birth = input('What is your date of birth ')
    town = input('In what city do you live ')
    email = input('What is your email ')
    tel = input('what is your phone # ')
    return name, last_name, date_birth, town, email, tel
print(user_info())