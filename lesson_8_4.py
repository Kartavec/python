# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

class Warehouse:

    def __init__(self):
        self.name = ''
        self.address = ''
        self.goods = {}


class Good:
    def __init__(self, model='', type_='', purchase_price=0.0, sale_price=0.0):
        self.model = model
        self.type = type_
        self.purchase_price = purchase_price
        self.sale_price = sale_price


class Printer(Good):
    def __init__(self, model='', purchase_price=0.0, sale_price=0.0):
        super().__init__(self, model, 'printer', purchase_price, sale_price)


class Scaner(Good):
    def __init__(self, model='', purchase_price=0.0, sale_price=0.0):
        super().__init__(self, model, 'scaner', purchase_price, sale_price)

class Copier(Good):
    def __init__(self, model='', purchase_price=0.0, sale_price=0.0):
        super().__init__(self, model, 'copier', purchase_price, sale_price)
