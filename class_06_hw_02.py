# Class 06
# Task 02
# A  script that creates Road class with length and width as attributes.

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width


class MassCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume


roady = MassCount(25, 10000, 125)
print(roady.mass())
