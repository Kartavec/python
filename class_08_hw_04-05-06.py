# Class 08
# Task 04-05-06
# A  script that creates StoreMashines class


class StoreMashines:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Model name': self.name, 'Price per unit': self.price, 'Quantity': self.quantity}

    def __str__(self):
        return f'{self.name} proce {self.price} quantity {self.quantity}'

    # @classmethod
    # @staticmethod
    def reception(self):
        # print(f'To exit press - Q, continue - Enter')
        # while True:
        try:
            unit = input(f'Enter product ')
            unit_p = int(input(f'Price per unit '))
            unit_q = int(input(f'Price quantity '))
            unique = {'Model name': unit, 'Price per unit': unit_p, 'Quantity': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Current list -\n {self.my_store}')
        except:
            return f'Input error'

        print(f'To exit press - Q, continue - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'All warehouse -\n {self.my_store_full}')
            return f'Exit'
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(StoreMashines):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(StoreMashines):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())
