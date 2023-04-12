class Worker():
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)
    def get_full_name(self):
        print(f'The name of employee is {self.name.title()} {self.surname.title()}.')
    def get_total_income(self):
        worker_wage = self._income['wage'] + self._income['bonus']
        print(f'His salary is {worker_wage}$.')

ceo_income_list = {'wage' : 1200, 'bonus' : 500}
worker_income_list = {'wage' : 700, 'bonus' : 250}

myworker = Position('ivan', 'ivanov', 'CEO', ceo_income_list)
myworker.get_full_name()
myworker.get_total_income()

myworker = Position('roman', 'romanov', 'worker', worker_income_list)
myworker.get_full_name()
myworker.get_total_income()
