from abc import ABC, abstractmethod
import math


class Clothes():

    def __init__(self, anthropometric_data):
        self.anthropometric_data = anthropometric_data

    @abstractmethod
    def consumption(self, anthropometric_data):
        pass


class Coat(Clothes):

    def __init__(self, anthropometric_data):
        self.anthropometric_data = anthropometric_data

    @property
    def consumption(self):
        consumption = round((self.anthropometric_data / 6.5 + 0.5), 2)
        return (f'To sew such coat we need {consumption} units of textile.')


class Costume(Clothes):
    def __init__(self, anthropometric_data):
        self.anthropometric_data = anthropometric_data

    @property    
    def consumption(self):
        consumption = round((self.anthropometric_data * 2 + 0.3), 2)
        return (f'To sew such costume we need {consumption} units of textile.')


coat = Coat(10)
print(coat.consumption)

costume = Costume(150)
print(costume.consumption)
