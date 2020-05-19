import sys

from menu_items import menu_item_1, menu_item_2, menu_item_3, menu_item_4, menu_item_5, menu_item_6


def show_menu():
    menu_items = {
        '1': 'Переменные',
        '2': 'Секунды',
        '3': 'Сумма чисел',
        '4': 'Большая цифра',
        '5': 'Прибыль и издержка',
        '6': 'Пробежки',
        '0': 'Выход'
    }

    for item in menu_items:
        print(f'{item}: {menu_items[item]}')

    choice = input(" >>  ")
    exec_menu(choice)
    return


def exec_menu(choice):
    menu_actions = {
        '1': menu_item_1,
        '2': menu_item_2,
        '3': menu_item_3,
        '4': menu_item_4,
        '5': menu_item_5,
        '6': menu_item_6,
        '0': close_cli
    }

    if choice == '':
        show_menu()
    else:
        try:
            menu_actions[choice]()
        except KeyError:
            print("Некорректный пункт меню, попробуйте снова.")
            print()
    return


def close_cli():
    sys.exit()
