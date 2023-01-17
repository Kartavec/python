
class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())

first_person = Position ( 'Анатолий', 'Иванов','Менеджер', 12000, 1000)
print(first_person.get_full_name(), first_person.get_total_income())
