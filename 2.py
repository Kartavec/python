
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def count_asphalt_mass(self, mass_m2, depth):
        return self._length * self._width * mass_m2 * depth


r1 = Road(20, 5000)

