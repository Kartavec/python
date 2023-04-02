"""
Задание2.
Реализовать проект расчёта суммарного расхода ткани на производство
одежды. Основная сущность (класс) этого проекта — одежда, которая
может иметь определённое название. К типам одежды в этом проекте
относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут
быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать
формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике
полученные на этом уроке знания: реализовать абстрактные классы
для основных классов проекта, проверить
на практике работу декоратора @property.
"""


from abc import ABC, abstractmethod


class Clothing(ABC):
    @abstractmethod
    def textile_calc(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass


class Coat(Clothing):
    def __init__(self, size: float, name):
        if not isinstance(size, float):
            print('задайте размер числом')
            raise ValueError
        self.__size = size
        self.__name = name

    def textile_calc(self):
        return self.__size / 6.5 + 0.5

    @property
    def name(self):
        return f'Пальто {self.__name}'


class Suit(Clothing):
    def __init__(self, height: float, name):
        if not isinstance(height, float):
            print('задайте размер числом')
            raise ValueError
        self.__height = height
        self.__name = name

    def textile_calc(self):
        return self.__height * 2 + 0.3

    @property
    def name(self):
        return f'{self.__name}'


suit01 = Suit(175.2, 'Пальто')
coat01 = Coat(50.0, 'Костюм')

print(suit01.name)
print(f'Для пошива {suit01.name} потребуется {coat01.textile_calc()}')
