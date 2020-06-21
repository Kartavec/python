from task04.office import Office
from task04.warehouse import Warehouse
from task04.departament import Departament
from task04.service_center import ServiceCenter


def print_storage(departament):
    if isinstance(departament, Departament):
        print(f'Оргтехника на складе {departament}:')
        print(departament.get_all_devices())
        print(f'Общее воличество: {departament.get_devices_count()}')
        print()
    else:
        print('Нет такого подразделения')


def make_pause(message):
    print('***********')
    input(f'{message} >> ENTER')


if __name__ == '__main__':
    make_pause('Создание складов')
    main_warehouse = Warehouse('Main warehouse')
    print_storage(main_warehouse)
    second_warehouse = Warehouse('Secondary warehouse')
    print_storage(second_warehouse)

    make_pause('Создание офиса')
    main_office = Office('Main office')
    print_storage(main_office)

    make_pause('Создание ошибочного заказа на закупку оргтехники через склада')
    order = {
        'xerа': 'erf',
    }
    print(order)
    main_warehouse.buy(order)

    make_pause('Создание корректного заказа')

    order = {
        'xerox': 5,
        'printer': 10,
        'scanner': 2,
        'monitor': 15,
        'desktop': 15
    }

    main_warehouse.buy(order)

    make_pause('Просмотр хранилища склада и офиса после заказа')
    print_storage(main_warehouse)
    print_storage(main_office)

    make_pause('Просмотр рандомного ксерокса, статус "NEW"')
    print(main_warehouse.storage['xerox'][0])
    print()

    make_pause('Создание заказа и поставка техники в офис')

    new_order = {
        'xerox': 3,
        'printer': 7,
        'scanner': 1,
        'monitor': 10,
        'desktop': 10
    }

    print(new_order)
    main_warehouse.supply(new_order, main_office)

    make_pause('Просмотр хранилища склада и офиса')
    print_storage(main_warehouse)
    print_storage(main_office)

    make_pause('Получить технику определённой категории хранилища по категории')
    print(f'Техника в офисе {main_office} категории "xerox"')
    print(main_office.get_devices_by_category('xerox'))
    print()

    make_pause('Проверка на правильность указания категории')
    print(main_office.get_devices_by_category('xerx'))
    print()

    make_pause('Поиск девайся по серийному номеру')
    serial_number = main_office.get_devices_by_category('printer')['printer'][0].serial_number
    print(main_office.get_device_by_serial(serial_number))
    print()

    make_pause('Просмотр рандомного принтера в офисе, статус сменился на "IN USE"')
    random_printer = main_office.storage['printer'][0]
    print(random_printer)

    make_pause('Просмотр уровня чернил принтера')
    print(random_printer.ink_level)

    make_pause('ЗАправка принтера чернилами')
    random_printer.ink_refill()
    print(random_printer.ink_level)

    make_pause('Печать на принтере 10 страниц')
    random_printer.print(10)
    print(random_printer.ink_level)

    make_pause('При уровне одного из чернил менее 20 процентов будет выдаваться предупреждение при каждой печати, при '
               'уровне одного из чернил менее 3 процентов, печать остановиться')
    random_printer.print(200)
    print()

    make_pause('Аналогичные операции доступны для ксерокса')
    random_xerox = main_office.storage['xerox'][0]
    print(random_xerox.toner_level)
    random_xerox.toner_refill()
    print(random_xerox.toner_level)
    random_xerox.print(600)
    print()

    make_pause('ТЕхника может поломаться и её можно отправить в сервисный центр')
    random_xerox.set_broken_status()
    print(random_xerox)

    main_service_center = ServiceCenter('Main Service Center')

    main_office.sent_device(main_service_center, random_xerox)

    print_storage(main_service_center)

    make_pause('В сервисном центре можно технику починить и оптравить обратно в офис')

    main_service_center.repair_device(random_xerox)
    print(random_xerox)

    main_service_center.sent_device(main_office, random_xerox)
    print(random_xerox)

    make_pause('Получение всех принтеров со статусом чернил "LOW"')
    for printer in main_office.storage['printer']:
        printer.ink_refill()
        printer.print(150)
    print(main_office.get_printers_low_ink())

    for printer in main_office.get_printers_low_ink():
        print(printer)
        print(printer.ink_status)
        print()

    make_pause('Аналогично для статуса "EMPTY"')
    for printer in main_office.storage['printer']:
        printer.ink_refill()
        printer.print(300)
    print(main_office.get_printers_low_ink())

    for printer in main_office.get_printers_empty_ink():
        print(printer)
        print(printer.ink_status)
        print()