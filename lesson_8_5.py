# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру, например словарь.
class Warehouse:

    def __init__(self):
        self.name = ''
        self.address = ''
        self.goods = {}

    def add_goods(self, good):
        if good.model not in self.goods:
            self.goods[good.model] = good
        else:
            self.goods[good.model].quantity += good.quantity

    def pop_goods(self, good):
        self.goods[good.model].quantity -= good.quantity


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
