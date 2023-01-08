"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс
«Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
(принтер, сканер, ксерокс). В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
оргтехники на склад и передачу в определённое подразделение компании. Для хранения данных
о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую
подходящую структуру (например, словарь).
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип
данных.
"""

import os
import sys
#from math import ceil
from sys import exit


class Warehouse:
    def __init__(self, capacity, address, warm_storage):
        self.capacity = capacity  # рабочий объем склада в паллетах
        self.address = address  # адрес склада
        self.warm_storage = warm_storage  # является ли теплым (True/False)

    """метод добавления склада как площадки, на которую будут поставятся грузы
       в папке с названием склада добавляется текстовый файл с его характеристиками
       при существлении погрузки в конце дня в характеристиках склада изменяется 
       доступный объем хранения"""

    def add_warehouse(self):  # добавляем склад для проведения операция с ним
        path = str(f'{self.address}')  # создаем директорию по адресу склада в корневой папке проекта
        try:
            os.makedirs(path)
        except OSError:
            print("Создать директорию %s не удалось, возможно, она уже существует" % path)
        else:
            print("Успешно создана директория %s " % path)

        with open(f'{path}/warehouse_spec.txt', 'w') as file:
            file.write(f'{self.capacity},{self.address},{self.warm_storage}')

    """метод производит поставку на склад. вызывается в коце дня, когда сформированы все запросы
    на доставку на этот склад"""

    def upload_warehouse(self, upload_date):
        path = str(f'{self.address}/{upload_date}')
        with open(f'{self.address}/warehouse_spec.txt', 'r+') as file_4:  # достаем из спецификации актуальную
            # емкость склада
            for line in file_4:
                spec_last = line    #добираемся до последней строки
            new_capacity = spec_last.split(',', 1)
            new_capacity = int(new_capacity[0])
            print(f'актуальая емкость склада {new_capacity}')

            files = f'full_pall.txt', f'remain_pall.txt'  # создаем кортеж для перебора файлов
            for file in files:  # перебираем строки в обоих файлах
                with open(f'{self.address}/storage.txt', 'a') as file_2:  # файл отображающий товары на складе
                    with open(f'{path}/{file}', 'r') as file_3:
                        for line in file_3:
                            file_2.write(line)
                            line = line.split(',', 1)
                            line = int(line[0])
                            new_capacity = new_capacity - line
                os.rename(f'{path}/{file}',  # переименовываем отработаные файлы
                          f'{path}/uploaded_{file}')
            print(f'конечная емкость склада после отгрузки {new_capacity}')
            file_4.write(f'\n{new_capacity},{self.address},{self.warm_storage},{upload_date}')


    """метод производит поставку на склад. вызывается в коце дня, когда сформированы все запросы
    на доставку на этот склад"""


    def download_warehouse(self, vendor, model):
        with open(f'{self.address}/storage.txt', 'r') as file_5:  #открываем файл отображающий товары на складе
            count = False
            for line in file_5:
                line = line.split(',')
                storage_vendor = line[3]    #вытягиваем из списка производителя
                storage_model = line[4]     #вытягиваем из списка модель
                if vendor == storage_vendor and model == storage_model:
                    count = True   #переменная, свидетельствующая о наличии товара на складе
            if count == True:
                print(f'поставка со склада {self.address} модели {vendor} {model} возможна')
            else:
                print(f'на складе {self.address} нет необходимого товара')


class MyExc(Exception):
    def __init__(self, txt):
        self.txt = txt


class OfficeEquipment:
    def __init__(self, type, supplier, origin_country, vendor, model, pallett_quantity, mass,
                 warm_storage=True):
        self.type = type  # тип оргтехники
        self.supplier = supplier  # продавец
        self.origin_country = origin_country  # страна происхождения
        self.vendor = vendor  # производитель
        self.model = model  # модель

        try:
            if isinstance(pallett_quantity, int):
                self.pallett_quantity = pallett_quantity  # количество единиц на паллете, шт.
            else:
                raise MyExc("количество товаров на паллете должно быть целым числом")
        except MyExc as error:
            print(error.txt)
            sys.exit(0)

        self.mass = mass  # масса брутто единицы, кг


class Printers(OfficeEquipment):
    def __init__(self, supplier, origin_country, vendor, model, pallett_quantity,
                 mass, laser, colors, warm_storage):
        super().__init__(supplier, origin_country, warm_storage, vendor, model, pallett_quantity, mass)
        self.laser = laser  # является ли лазерным (True/False)
        self.colors = colors  # количество цветов кроме черного "0" - черно-белый

    def shipment(self, shipment_quantity, shipment_address, shipment_date):
        path = str(f'{shipment_address}/{shipment_date}')  # создаем директорию по адресу склада в корневой
        try:  # папке проекта и директорию по дате поставки
            os.makedirs(path)  # в папке склада
        except OSError:
            print("Создать директорию %s не удалось, возможно, она уже существует" % path)
        else:
            print("Успешно создана директория %s " % path)

        pallet_num = shipment_quantity // self.pallett_quantity  # определяем количество
        # целых паллетов
        print(f'количество целых паллетов {pallet_num}')
        shipment_remains = shipment_quantity % self.pallett_quantity \
                           / self.pallett_quantity  # определяем остаток места в долях от
        # целого палета
        print(f'остаток груза в долях от целого палета {shipment_remains}')
        quantity_remain = int(shipment_remains * self.pallett_quantity)  # остаток для
        # отгрузки в штуках
        print(f'остаток в штуках {quantity_remain}')

        file = open(f'{path}/full_pall.txt', 'a')  # создаем файл, в который будем записывать целые палеты
        file.write(f'{pallet_num},{self.supplier},{self.origin_country},{self.vendor},'
                   f'{self.model},{self.pallett_quantity},{self.mass},'
                   f'{self.pallett_quantity}\n')  # записываем строку с целыми палетами текущей поставки
        file.close()

        file = open(f'{path}/remain_pall.txt', 'a+')  # создаем файл, в который будем записывать
        # остатки с палеты, или дописываем его
        if os.stat(f'{path}/remain_pall.txt').st_size != 0:  # проверяем пустой файл или нет
            print('file is not empty')
            with open(f'{path}/remain_pall.txt', 'r') as file_1:  # считываем последнюю строку
                for line in file_1:
                    row = line
            print(type(row))
            print(f'последняя строка в остатках {row}')
            last_remain = row.split(',', 2)  # разбиваем строку по запятым до листа
            print(last_remain)
            last_remain = float(last_remain[1])  # берем первое значение из листа - степень заполненности паллета
            print(f'палет заполнен на {last_remain}')
            print(type(last_remain))

            add = int((1 - last_remain) * self.pallett_quantity)  # проверяем, сколько единиц товара
            # можно доложить в неполный паллет
            print(f'можно доложить {add} шт.')
            if add > quantity_remain:
                print('пустого места больше чем остаток отгрузки')
                last_remain = last_remain + quantity_remain / self.pallett_quantity  # добавляем в паллет
                # остаток товара отгрузки
                print(f'теперь палет заполнен на {last_remain}')
                file.write(f'0,{(last_remain)},{self.supplier},{self.origin_country},'
                           f'{self.vendor},{self.model},{self.pallett_quantity},{self.mass},'
                           f'{quantity_remain}\n')  # вписываем то, что догружаем в неполный паллет
            else:
                print('пустого места меньшее чем остаток отгрузки')
                last_remain = last_remain + add / self.pallett_quantity
                print(f'теперь заполненность палета{last_remain}')
                file.write(f'0,{last_remain / self.pallett_quantity},{self.supplier},{self.origin_country},'
                           f'{self.vendor},{self.model},{self.pallett_quantity},{self.mass},'
                           f'{add}\n')  # вписываем то, что догружаемв неполный паллет
                quantity_remain = quantity_remain - add  # вычисляем количество шт. к отгрузке
                print(f'теперь остаок отгрузки {quantity_remain} шт.')
                file.write(f'1,{quantity_remain / self.pallett_quantity},{self.supplier},{self.origin_country},'
                           f'{self.vendor},{self.model},{self.pallett_quantity},{self.mass},'
                           f'{quantity_remain}\n')  # вписываем строку с новым недозаполненым паллетом
        else:
            print('file is empty')
            file.write(f'1,{shipment_remains},{self.supplier},{self.origin_country},{self.vendor},{self.model},'
                       f'{self.pallett_quantity},{self.mass},{quantity_remain}\n')  # вписываем строку
            # остаток от текущей поставки
        file.close()


class Monitors(OfficeEquipment):
    def __init__(self, supplier, origin_country, warm_storage, vendor, model, pallett_quantity,
                 mass, is_flat, diagonal):
        super().__init__(supplier, origin_country, warm_storage, vendor, model, pallett_quantity, mass)
        self.is_flat = is_flat  # является ли жидкокриталличским (True/False)
        self.diagonal = diagonal  # диагональ экрана в дюймах


class phone(OfficeEquipment):
    def __init__(self, supplier, origin_country, warm_storage, vendor, model, pallett_quantity,
                 mass, line_num, is_ip, is_wire):
        super().__init__(supplier, origin_country, warm_storage, vendor, model, pallett_quantity,
                         mass)
        self.line_num = line_num  # количество линий
        self.is_ip = is_ip  # является ли IP-телефоном
        self.is_wire = is_wire  # является ли проводным


hp3322 = Printers('Print Ltd', 'China', 'HP', '3322', 35, 16.3, True, False, True) #определяем экземпляр с товаром

hp3322.shipment(5896, "BCN_Sants", '05.01.2023') #составляем заявку для поставки на склад

bcn_sants = Warehouse(1700, 'BCN_Sants', True) #создаем склад

bcn_sants.add_warehouse() #добавляем данные о складе

bcn_sants.upload_warehouse('05.01.2023') #осуществляем поставку на склад

bcn_sants.download_warehouse('HP', '3322') #проверяем возможность отгрузки со склада
