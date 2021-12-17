# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

class Date:
    def __init__(self, date: str):
        self.date = date
        self.day = 0
        self.month = 0
        self.year = 0

    @classmethod
    def set_date(cls, obj):
        obj.day = obj.date.split('-')[0]
        obj.month = obj.date.split('-')[1]
        obj.year = obj.date.split('-')[2]

    @staticmethod
    def check_date(date: str, day=True, month=True, year=True) -> bool:
        if day and month and year:
            if Date.check_date(date, day=True, month=False, year=False) and\
               Date.check_date(date, day=False, month=True, year=False) and\
               Date.check_date(date, day=False, month=False, year=True):
                return True
        elif day:
            # проверка без учета месяца
            if 1 <= int(date.split('-')[0]) <=31:
                return True
        elif month:
            if 1 <= int(date.split('-')[1]) <= 12:
                return True
        elif year:
            if 1 <= int(date.split('-')[2]):
                return True
        else:
            return False

    def __str__(self):
        return f'Хранимая дата: {self.day}-{self.month}-{self.year}'


date = "22-01-1996"
dt = Date(date)
if Date.check_date(dt.date, day=True, month=True, year=True):
    dt.set_date(dt)
    print(dt)
