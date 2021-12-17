# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
# уроках по ООП.


class Warehouse:

    def __init__(self, name='', address=''):
        self.name = name
        self.address = address
        self.goods = {}

    def add_goods(self, good):
        if good.model not in self.goods:
            self.goods[good.model] = good
        else:
            self.goods[good.model].quantity += good.quantity

    def pop_goods(self, good):
        self.goods[good.model].quantity -= good.quantity

    def get_stat(self):
        return [(good.model, good.quantity) for good in self.goods.values()]


class Good:
    def __init__(self, model='', type_='', purchase_price=0.0, sale_price=0.0, quantity=0):
        self.model = model
        self.type = type_
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.sale_price = sale_price


class Printer(Good):
    def __init__(self, model='', purchase_price=0.0, sale_price=0.0, quantity=0):
        super().__init__(self, model, 'printer', purchase_price, sale_price, quantity)


class Scaner(Good):
    def __init__(self, model='', purchase_price=0.0, sale_price=0.0, quantity=0):
        super().__init__(self, model, 'scaner', purchase_price, sale_price, quantity)


class Copier(Good):
    def __init__(self, model='', purchase_price=0.0, sale_price=0.0, quantity=0):
        super().__init__(self, model, 'copier', purchase_price, sale_price, quantity)
