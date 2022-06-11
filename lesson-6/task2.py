class Road:
    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def calc_asphalt_weight(self, weight_pm: int = 25, depth: int = 5):
        return self._width * self._length * weight_pm * depth


road = Road(20, 5000)
print(road.calc_asphalt_weight())
