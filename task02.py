import sys


def print_list(user_list):
    for item in user_list:
        print(item)


def add_item(user_list, element):
    user_list.append(element)
    return user_list


def reverse_items(user_list):
    for number in range(0, len(user_list) - 1, 2):
        user_list[number], user_list[number + 1] = user_list[number + 1], user_list[number]


def show_items(user_list):
    for item in user_list:
        print(item)


def menu(user_list):
    menu_items = {
        '1': 'Добавить элемент списка',
        '2': 'Посмотреть элементы списка',
        '3': 'Развернуть элементы списка',
        '0': 'Выход'
    }

    for item in menu_items:
        print(f'{item}: {menu_items[item]}')

    choice = input(" >>  ")
    exec_menu(choice, user_list)
    return


def menu_item_1(user_list):
    list_item = input('Введите элемент списка для добавления:')
    add_item(user_list, list_item)
    print()


def menu_item_2(user_list):
    print('В списке сейчас слеудющие пункты:')
    for item in user_list:
        print(item)
    print()


def menu_item_3(user_list):
    print('Элементы до обмена:')
    print_list(user_list)

    reverse_items(user_list)

    print('Элементы после обмена')
    print_list(user_list)
    print()


def exec_menu(choice, user_list):
    if choice == '1':
        menu_item_1(user_list)
    elif choice == '2':
        menu_item_2(user_list)
    elif choice == '3':
        menu_item_3(user_list)
    elif choice == '0':
        exit()
    else:
        print('Некорректный ввод, попробуйте еще раз')


def close_cli():
    sys.exit()


if __name__ == '__main__':
    my_list = []
    while True:
        menu(my_list)
