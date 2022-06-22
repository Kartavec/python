import datetime
import random
import string

from warehouse import models

BRANDS_LIST = ['Canon', 'LG', 'Philips', 'Xiaomi']


def generate_model_name():
    return '%s (%s)' % (
        random.choice(BRANDS_LIST),
        random.choices(string.ascii_uppercase + string.digits, k=8)
    )


def generate_equip():
    cls = random.choice(models.Equipment.__subclasses__())
    return cls(
        model=generate_model_name(),
        year=random.randint(2000, datetime.date.today().year),
        is_new=random.choice([True, False, True])
    )


equipments = [generate_equip() for i in range(10)]

eq_1 = equipments[0]
eq_2 = equipments[1]

deparment_1 = models.Department('Department 1')
deparment_2 = models.Department('Department 2')
warehouse = models.Warehouse('Main')

warehouse.append_list(equipments)
print('==== WAREHOUSE BALANCE ====')
warehouse.balance()
print('==================')
warehouse.append(eq_1)

warehouse.move_equipment(eq_1, deparment_1)
warehouse.move_equipment(eq_2, deparment_1)
warehouse.move_equipment(eq_1, deparment_2)
print('========= DEPARTMENT 1 BALANCE =========')
deparment_1.balance()
print('==================')

try:
    warehouse.move_equipments(models.Printer.__name__, deparment_2, 2)
except AssertionError as e:
    print('На складе нет столько техники')
print('========= DEPARTMENT 2 BALANCE =========')
deparment_2.balance()
print('==================')
