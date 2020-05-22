def split_string(user_string):
    splited_string = user_string.split()
    return splited_string


def print_strings(strings):
    for item in enumerate(strings):
        if len(item[1]) > 10:
            print(f'{item[0]} {item[1][:10]}')
        else:
            print(f'{item[0]} {item[1]}')


if __name__ == '__main__':
    user_string = input('Введите строку:')
    splited_string = split_string(user_string)
    print_strings(splited_string)
