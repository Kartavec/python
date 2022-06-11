class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return '%s %s' % (self.name, self.surname)

    def get_total_income(self):
        try:
            return self._income['wage'] + self._income['bonus']
        except TypeError:
            print('Income dict error')
        return 0


worker_1 = Position('NAME', 'SURNAME', 'POSITION', {"wage": 1234, "bonus": 5678})
print(worker_1.get_full_name())
print(worker_1.get_total_income())
