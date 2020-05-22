import sys


def get_last_good_number(goods):
    return goods[-1][0]


def add_item(goods):
    current_number = get_last_good_number(goods) + 1
    title = input('Название товара:')
    price = input('Цена товара:')
    quantity = input('Количество товара:')
    unit = input('Единица измерения:')
    text = f'Вы желаете добавить {quantity} {unit} товар "{title} по цене {price} под номером {current_number}? Y/N"'
    confirmation = input(text)
    if confirmation.lower() == 'y':
        new_item = (
            current_number, {'название': title, 'цена': price, 'количество': quantity, 'ед': unit}
        )
        goods.append(new_item)


def print_list(goods):
    for item in goods:
        print(item)


def print_dict(dictionary):
    for name, value in dictionary.items():
        print(f'{name} - {value}')


def get_statistic(goods):
    result = {
        'название': [],
        'цена': [],
        'количество': [],
        'ед': []
    }
    for item in goods:
        stats = item[1]
        for stat_name in stats:
            if stats[stat_name] not in result[stat_name]:
                result[stat_name].append(stats[stat_name])
    return result


def menu(user_list):
    menu_items = {
        '1': 'Добавить товар',
        '2': 'Посмотреть товары',
        '3': 'Посмотреть статистику',
        '0': 'Выход'
    }

    for item in menu_items:
        print(f'{item}: {menu_items[item]}')

    choice = input(" >>  ")
    exec_menu(choice, user_list)
    return


def menu_item_1(goods):
    add_item(goods)
    print()


def menu_item_2(goods):
    print('В базе данных сейчас ледующие товары:')
    print_list(goods)
    print()


def menu_item_3(goods):
    print('Cтатистика по товарам:')
    statistic = get_statistic(goods)
    print_dict(statistic)
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
    goods = [
        (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед': 'шт.'}),
        (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'ед': 'шт.'}),
        (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'ед': 'шт.'})]
    while True:
        menu(goods)
