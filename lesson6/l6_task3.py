class Worker:

    def __init__(self,
                 name: str, surname: str,
                 position: str, wage: float,
                 bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(self.name + ' ' + self.surname)

    def get_total_income(self):
        print('$' + str(sum(self._income.values())))


employee1 = Position('Вадим', 'Крякин', 'system administrator', 2500, 400)
employee2 = Position('Зилола', 'Давронова', 'sales consultant', 1100, 100)

employee1.get_full_name()
employee1.get_total_income()
employee2.get_full_name()
employee2.get_total_income()
