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


if __name__ == '__main__':
    # Создание складов
    main_warehouse = Warehouse('Main warehouse')
    second_warehouse = Warehouse('Secondary warehouse')

    # Создание офиса
    main_office = Office('Main office')

    # Создание ошибочного заказа на закупку оргтехники через склад
    order = {
        'xerа': 'erf',
    }

    main_warehouse.buy(order)

    # Создание корректного заказа

    order = {
        'xerox': 5,
        'printer': 10,
        'scanner': 2,
        'monitor': 15,
        'desktop': 15
    }

    main_warehouse.buy(order)

    # Просмотр хранилища склада и офиса
    print_storage(main_warehouse)
    print_storage(main_office)

    # Просмотр рандомного ксерокса, статус 'NEW'
    print(main_warehouse.storage['xerox'][0])
    print()

    # Создание заказа и поставка техники в офис

    new_order = {
        'xerox': 3,
        'printer': 7,
        'scanner': 1,
        'monitor': 10,
        'desktop': 10
    }

    main_warehouse.supply(new_order, main_office)

    # Просмотр хранилища склада и офиса
    print_storage(main_warehouse)
    print_storage(main_office)

    # Получить технику определённой категории хранилища по категории
    print(f'Техника в офисе {main_office} категории "xerox"')
    print(main_office.get_devices_by_category('xerox'))
    print()

    # Проверка на правильность указания категории
    print(main_office.get_devices_by_category('xerx'))
    print()

    # Поиск девайся по серийному номеру
    serial_number = main_office.get_devices_by_category('printer')['printer'][0].serial_number
    print(main_office.get_device_by_serial(serial_number))
    print()

    # Просмотр рандомного принтера в офисе, статус сменился на 'IN USE'
    random_printer = main_office.storage['printer'][0]
    print(random_printer)

    # Просмотр уровня чернил принтера
    print(random_printer.ink_level)

    # ЗАправка принтера чернилами
    random_printer.ink_refill()
    print(random_printer.ink_level)

    # Печать на принтере 10 страниц
    random_printer.print(10)
    print(random_printer.ink_level)

    # При уровне одного из чернил менее 20 процентов будет выдаваться предупреждение при каждой печати,
    # при уровне одного из чернил менее 3 процентов, печать остановиться
    random_printer.print(200)
    print()

    # Аналогичные операции доступны для ксерокса
    random_xerox = main_office.storage['xerox'][0]
    print(random_xerox.toner_level)
    random_xerox.toner_refill()
    print(random_xerox.toner_level)
    random_xerox.print(600)
    print()

    # ТЕхника может поломаться и её можно отправить в сервисный центр
    random_xerox.set_broken_status()
    print(random_xerox)

    main_service_center = ServiceCenter('Main Service Center')

    main_office.sent_device(main_service_center, random_xerox)

    print_storage(main_service_center)

    # В сервисном центре можно технику починить и оптравить обратно в офис

    main_service_center.repair_device(random_xerox)
    print(random_xerox)

    main_service_center.sent_device(main_office, random_xerox)
    print(random_xerox)

    print(random_xerox.__dict__)
    print(random_printer.ink_level)