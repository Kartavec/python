import random


class Department:
    def __init__(self, name: str):
        assert len(name) > 0
        self.name = name
        self._storage = []
        self._counts = {cls.__name__: 0 for cls in Equipment.__subclasses__()}

    def append(self, equipment):
        assert issubclass(equipment.__class__, Equipment)
        if not self.find_in_storage(equipment):
            self._storage.append(equipment)
            self._counts[equipment.__class__.__name__] += 1
        else:
            print('Техника уже на складе')

    def append_list(self, equipments):
        for equipment in equipments:
            self.append(equipment)

    def remove(self, equipment):
        assert issubclass(equipment.__class__, Equipment)
        if self.find_in_storage(equipment):
            self._storage.remove(equipment)
            self._counts[equipment.__class__.__name__] -= 1
            return True
        return False

    def find_in_storage(self, equipment):
        assert issubclass(equipment.__class__, Equipment)
        return next((x for x in self._storage if x == equipment), None)

    def get_all(self, equipment_type):
        # return [x for x in self._storage if x.__class__ == equipment_type]
        for x in self._storage:
            if x.__class__.__name__ == equipment_type:
                yield x

    def balance(self):
        for cls, cnt in self._counts.items():
            print(f'{cls}: {cnt}')


class Warehouse(Department):

    def move_equipment(self, equipment, department):
        if self.remove(equipment):
            department.append(equipment)
        else:
            print('На складе нет необходимой техники')

    def back_equipment(self, equipment, department):
        if department.remove(equipment):
            self.append(equipment)
        else:
            print('В отделении нет необходимой техники')

    def move_equipments(self, equipment_type, deparmet, count):
        assert self._counts[equipment_type] >= count
        for equipment in self.get_all(equipment_type):
            self.move_equipment(equipment, deparmet)


class Equipment:
    def __init__(self, model: str, year: int, is_new: bool):
        self.serial = random.randint(10000, 999999)  # серийный номер
        self.model = model  # модель
        self.year = year  # год выпуска
        self.is_new = is_new  # новый/бу
        self.is_broken = False

    def __str__(self):
        return f'{self.serial} {self.model} {self.year}'

    def broke(self):
        print('Упс! Устройство сломалось')
        self.is_broken = True

    def repair(self):
        self.is_broken = False
        self.is_new = False

    def action(self):  # действие устройства
        if random.randint(0, 100) < 10:
            self.broke()
        return True

    def __eq__(self, other):
        return isinstance(other, self.__class__) and other.serial == self.serial


class Printer(Equipment):
    def __init__(self, model, year, is_new):
        super().__init__(model, year, is_new)
        self._ink = {'r': 0, 'g': 0, 'b': 0}  # черлила

    def refuel(self):
        self._ink = {'r': 100, 'g': 100, 'b': 100}

    def action(self):
        if not self.can_print():
            self._empty_ink_signal()
            return False
        # при печати принтер тратит бумагу
        for k, ink in self._ink.items():
            self._ink[k] = random.randint(0, ink - 10) if ink - 10 > 0 else 0
        return super().action()

    def can_print(self):
        ret = True
        for ink in self._ink:
            ret &= ink > 0
        return ret

    def _empty_ink_signal(self):
        print('Кончились чернила, необходимо замена')


class Fax(Equipment):
    def __init__(self, model, year, is_new):
        super().__init__(model, year, is_new)
        self._papers = 100

    def action(self):
        if self._papers == 0:
            print('Закончилась бумага')
            return False
        self._papers -= random.randint(1, self._papers)
        return super().action()


class Scaner(Equipment):
    def action(self):
        print('Сканирование...')
        return super().action()


class Xerox(Equipment):
    def action(self):
        print('Ксерокопирование...')
        return super().action()
