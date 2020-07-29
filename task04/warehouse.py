import random

from task04.departament import Departament
from task04.office_equipment import classes

models_in_stock = {
    'xerox': (
        ('Xerox', 'WorkCentre 3335'),
        ('KYOCERA', 'ECOSYS M2735dn'),
        ('Brother', 'MFC-L5700DN')
    ),
    'printer': (
        ('Epson', 'WorkForce WF-7710DWF'),
        ('Canon', 'i-SENSYS MF264dw'),
        ('HP', 'Neverstop Laser 1200n')
    ),
    'scanner': (
        ('Canon', 'CanoScan LiDE 400'),
        ('HP', 'Scanjet Professional 3000'),
        ('Epson', 'Perfection V370 Photo')
    ),
    'monitor': (
        ('Samsung', 'S24E390HL'),
        ('DELL', 'UltraSharp U2718Q Black'),
        ('Lenovo', 'ThinkVision Y44w-10 65EARAC1EU')
    ),
    'desktop': (
        ('LENOVO', 'IdeaCentre 510-15ICK'),
        ('MSI', 'Cubi N 8GL-037RU'),
        ('Acer', 'Veriton ES2730G')
    )
}


def check_order(order):
    for category in order:
        if category not in classes:
            return False

    for category in order:
        if not isinstance(order[category], int) and order[category] <= 0:
            return False
    return True


class Warehouse(Departament):

    def supply(self, order, office):
        if not check_order(order):
            print('Неправильный формат заказа.')
            return
        for category in order:
            for _ in range(order[category]):
                device = random.choice(self.storage[category])
                device.set_in_use_status()
                self.storage[category].remove(device)
                office.add_device(device)

    def buy(self, order):
        if not check_order(order):
            print('Неправильный формат заказа.')
            return
        for category in order:
            for _ in range(order[category]):
                brand, model = random.choice(models_in_stock[category])
                new_item = classes[category](brand, model)
                self.storage[category].append(new_item)

    def dump(self, category, device):
        self.storage[category].remove(device)