class Road():

    def __init__(self, length, width):
        self._length = length
        self._width = width
    
    def mass_calculation(self):
        unit_mass = 50
        thickness = 10
        result_mass = self._length * self._width * unit_mass * thickness
        print(f'The required asphalt mass for creating a road length of \
{self._length}m, width of {self._width}m and thickness of {thickness}сm \
is {result_mass} kg.')

my_road = Road(100, 10)
my_road.mass_calculation()