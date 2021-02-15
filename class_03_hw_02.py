# Class 03
# Task 02
# A simple function that takes 6 parameters of personal data as named args.
# The function prints out personal data in one string .

def print_user_data(**user_data):
    print(f'name: {user_data.get("name")}, last_name: {user_data.get("last_name")},'
          f' birth_year: {user_data.get("birth_year")}, city: {user_data.get("city")},'
          f' email: {user_data.get("email")}, phone: {user_data.get("phone")}')


if __name__ == '__main__':
    user = {
        'name': 'Steven',
        'last_name': 'King',
        'birth_year': '1954',
        'city': 'New York',
        'email': 'steven.king@yahoo.com',
        'phone': '985-111-00-45',
    }

print_user_data(**user)

