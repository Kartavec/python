class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_asphalt_mass(self):
        mass_on_m2 = 25
        thickness = 5
        mass = self._width * self._length * mass_on_m2 * thickness
        return mass


if __name__ == '__main__':
    my_road = Road(200, 300)
    print(my_road.calculate_asphalt_mass())
