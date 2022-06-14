from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def calc(self):
        pass


class Coat(Cloth):
    def __init__(self, v):
        self.__v = v

    @property
    def calc(self):
        return self.__v / 6.5 + 0.5


class Suit(Cloth):
    def __init__(self, h):
        self.__h = h

    @property
    def calc(self):
        return self.__h * 2 + 0.3


print(Coat(10).calc)
print(Suit(8).calc)
