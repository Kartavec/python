
class Road:
    __asphalt_mass = 25

    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)

    def asphalt_sum(self, thickness=1):
        return self._length * self._width * self.__asphalt_mass * thickness

road = Road(20, 5000)
calculation = road.asphalt_sum(5)
print(calculation)