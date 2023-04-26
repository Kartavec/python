# Доступно распределение техники по отделениям офиса, названия которых
# соответствуют типу техники, или на cклад. Информация о характеристиках
# созданных типов оргтехники (показана на примере принтеров) и количестве
# оргтехники в подразделениях и на складе хранится в словарях.
# Валидация выполнена при помощи оператора условия (показана на примере
# принтеров, предназначенных для офиса).

class Store():

    def __init__(self, item):
        self.item = str(item)

    @staticmethod
    def allocation_items(item, amount, where):
        if type(amount) != int:
            print('You need enter the number as amonut of equipment units!\n')
        elif "Printer" in str(type(item)) and where == 'office':
            allocation['printing_department'] += amount
        elif "Scanner" in str(type(item)) and where == 'office':
            allocation['scan_department'] += amount
        elif "Copier" in str(type(item)) and where == 'office':
            allocation['copy_department'] += amount
        elif "Printer" in str(type(item)) and where == 'store':
            allocation['printers_in_store'] += amount
        elif "Scanner" in str(type(item)) and where == 'store':
            allocation['scanners_in_store'] += amount
        elif "Copier" in str(type(item)) and where == 'store':
            allocation['copiers_in_store'] += amount
        print(f'{allocation}\n')


class Equipment():

    def __init__(self, manufacturer, color, purchase_date):
        self.color = color
        self.manufacturer = manufacturer
        self.purchase_date = purchase_date


class Printer(Equipment):

    def __init__(self, amount, manufacturer, color, purchase_date, print_speed,
                 print_format):
        self.amount = amount
        self.print_speed = print_speed
        self.print_format = print_format
        super().__init__(manufacturer, color, purchase_date)

    def information(self):
        item_info = {'amount': self.amount,
                     'manufacturer': self.manufacturer, 'color': self.color,
                     'purchase_date': self.purchase_date,
                     'print_speed': self.print_speed,
                     'print_format': self.print_format}
        return f'{item_info}\n'


class Scanner(Equipment):

    def __init__(self, amount, manufacturer, color, purchase_date,
                 dpi_resolution, color_depth):
        self.amount = amount
        self.dpi_resolution = dpi_resolution
        self.color_depth = color_depth
        super().__init__(manufacturer, color, purchase_date)

    def information(self):
        item_info = {'amount': self.amount,
                     'manufacturer': self.manufacturer, 'color': self.color,
                     'purchase_date': self.purchase_date, 
                     'dpi_resolution': self.dpi_resolution,
                     'color_depth': self.color_depth}
        return f'{item_info}\n'


class Copier(Equipment):

    def __init__(self, amount, manufacturer, color,
                 purchase_date, amount_copies_per_cycle, scaling):
        self.amount = amount
        self.amount_copies_per_cycle = amount_copies_per_cycle
        self.scaling = scaling
        super().__init__(manufacturer, color, purchase_date)

    def information(self):
        item_info = {'amount': self.amount,
                     'manufacturer': self.manufacturer, 'color': self.color,
                     'purchase_date': self.purchase_date,
                     'amount_copies_per_cycle': self.amount_copies_per_cycle,
                     'scaling': self.scaling}
        return f'{item_info}\n'


allocation = {'printing_department': 0, 'scan_department': 0,
              'copy_department': 0, 'printers_in_store': 0,
              'scanners_in_store': 0,
              'copiers_in_store': 0}

printers_type1 = Printer(10, 'Canon', 'yes', 2023, 40, 'A4')
print(f'Printers of type 1 characteristics - {printers_type1.information()}')
Store.allocation_items(printers_type1, 'five', 'office')
Store.allocation_items(printers_type1, 5, 'store')

scanners_type1 = Scanner(15, 'HP', 'no', 2020, 600, 8)
Store.allocation_items(scanners_type1, 7, 'store')
Store.allocation_items(scanners_type1, 8, 'office')

copiers_type1 = Copier(7, 'Ricoh', 'yes', 2022, 50, '1:4')
Store.allocation_items(copiers_type1, 4, 'store')
Store.allocation_items(copiers_type1, 3, 'office')
