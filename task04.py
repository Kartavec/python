from task04.office import Office
from task04.office_equipment import OfficeEquipment, Xerox, Printer
from task04.warehouse import Warehouse


if __name__ == '__main__':
    main_warehouse = Warehouse('Main')
    second_warehouse = Warehouse('Second')

    for warehouse in main_warehouse.instances():
        print(warehouse)

    second_warehouse.destroy()

    for warehouse in main_warehouse.instances():
        print(warehouse)

    new_xerox = Xerox('Xerox', 'MN-16')

    # xeroxes = (('Xerox', 'WorkCentre 3335'),
    #            ('KYOCERA', 'ECOSYS M2735dn'),
    #            ('Brother', 'MFC-L5700DN'))
    #
    # printers = (('Epson', 'WorkForce WF-7710DWF'),
    #             ('Canon', 'i-SENSYS MF264dw'),
    #             ('HP', 'Neverstop Laser 1200n'))
    #
    # scanners = (('Canon', 'CanoScan LiDE 400'),
    #             ('HP', 'Scanjet Professional 3000'),
    #             ('Epson', 'Perfection V370 Photo'))
    #
    # monitors = (('Samsung', 'S24E390HL'),
    #             ('DELL', 'UltraSharp U2718Q Black'),
    #             ('Lenovo', 'ThinkVision Y44w-10 65EARAC1EU'))
    #
    # desktops = (('LENOVO', 'IdeaCentre 510-15ICK'),
    #             ('MSI', 'Cubi N 8GL-037RU'),
    #             ('Acer', 'Veriton ES2730G'))

    my_wh = Warehouse('General')
    print(my_wh)

    order = {'xerox': 1,
             'printer': 999}

    my_wh.buy(order)

    for element in OfficeEquipment.instances():
        print(element)

    batch = {'xerox': 1,
             'printer': 25}

    main_office = Office('Main')
    print(main_office.storage)
    print(my_wh.storage)
    my_wh.supply(batch, main_office)

    print(main_office.storage)
    second_office = Office('Second')
    print(second_office.storage)

    serial_num = OfficeEquipment.instances()[1].serial_number

    print(my_wh.gei_device_by_serial(serial_num))
    verx = Xerox('noni', 'sdfsd')
    print(isinstance(verx, Xerox))

    random_printer = Printer.instances()[5]
    print(random_printer.__dict__)
    print(random_printer.ink_level)
    random_printer.ink_refill()
    print(random_printer.ink_level)

    random_printer.print(300)
    print(random_printer.ink_level)

    random_xerox = Xerox.instances()[1]

    print(random_xerox.toner_level)
    random_xerox.toner_refill()
    random_xerox.print(10)
    print(random_xerox.toner_level)
    random_xerox.print(1000)

