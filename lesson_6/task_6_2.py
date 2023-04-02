"""
Задание 2.
Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта,
необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для
покрытия одного кв. метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    def __init__(self, _length, _width, weight, height):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.height = height

    def count_mass(self):
        road_mass = (
            self._length * self._width * self.weight * self.height / 1000
        )
        print(f'Масса асфальта: 20м * 5000м * 25кг * 5см = {road_mass} т.')


build_road = Road(20, 5000, 25, 5)
build_road.count_mass()
