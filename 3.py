class Worker:
    def __init__(self, name, surname, position, income_dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income_dict


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


worker1 = Position('Petya', 'Pupkin', 'Lead programmist', {'wage': 5000, 'bonus': 3000})

print(worker1.get_full_name())
print(worker1.position)
print(worker1.get_total_income())
