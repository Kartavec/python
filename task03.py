class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        full_name = f'{self.name} {self.surname}'
        return full_name

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        return total_income


if __name__ == '__main__':
    new_income = {
        "wage": 1000,
        "bonus": 2000
    }

mp = Position('Александр',
              'Иванов',
              'Инженер',
              {
                  "wage": 1000,
                  "bonus": 2000
              })

print(mp.get_full_name())
print(mp.get_total_income())