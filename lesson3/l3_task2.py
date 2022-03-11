def personal_info(name, last_name, birth_place, residence, email, phone):
    print(name, last_name, birth_place, residence, email, phone)


personal_info(name=input('Name: '),
              last_name=input('Last name: '),
              birth_place=input('Place of birth: '),
              residence=input('City of residence: '),
              email=input('Email: '),
              phone=input('Phone number: '))
