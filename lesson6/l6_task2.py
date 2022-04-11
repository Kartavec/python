class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculation(self):
        value = (self.__length * self.__width * 25 * 5)/1000
        print(f'Необходимо {value} тонн асфальта для покрытия дороги.')


road1 = Road(2000, 10)
road2 = Road(3400, 20)
road1.calculation()
road2.calculation()
