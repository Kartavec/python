from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def cloth_consumption(self):
        pass


class Coat(Cloth):
    def __init__(self, size):
        self.size = size

    @property
    def cloth_consumption(self):
        return self.size / 6.5 + 0.5


class Costume(Cloth):
    def __init__(self, height):
        self.height = height

    @property
    def cloth_consumption(self):
        return self.height * 2 + 0.3


c1 = Coat(2)
print(c1.cloth_consumption)

c2 = Costume(5)
print(c2.cloth_consumption)
