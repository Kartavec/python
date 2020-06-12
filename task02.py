from abc import ABC, abstractmethod


class AbstractWear(ABC):
    def __init__(self, title):
        self.title = title

    "Вычисляем расход ткани в зависимости от одежды"
    @abstractmethod
    def consumption(self):
        pass


class Coat(AbstractWear):
    def __init__(self, title, size):
        super().__init__(title)
        self.size = size

    @property
    def consumption(self):
        return round((self.size / 6.5 + 0.5), 1)


class Suit(AbstractWear):
    def __init__(self, title, height):
        super().__init__(title)
        self.height = height

    @property
    def consumption(self):
        return round((2 * self.height + 0.3), 1)


class Fabric:
    common_consumption = 0

    def add_wear(self, wear):
        self.common_consumption += wear.consumption

    @property
    def consumption(self):
        return round(self.common_consumption, 1)


if __name__ == '__main__':
    my_coat = Coat('burb', 199)
    print(my_coat.title)
    print(my_coat.size)
    print(my_coat.consumption)

    my_suit = Suit('boss', 210)
    print(my_suit.title)
    print(my_suit.height)
    print(my_suit.consumption)

    my_fabric = Fabric()
    my_fabric.add_wear(my_suit)
    my_fabric.add_wear(my_coat)

    print(my_fabric.consumption)