import math


class Cage():

    def __init__(self, cell, cell_per_line):
        self.cell = cell
        self.cell_per_line = cell_per_line

    def __add__(self, other):
        res_cell = self.cell + other.cell
        return res_cell

    def __sub__(self, other):
        if self.cell > other.cell:
            res_cell = self.cell - other.cell
            return res_cell
        else:
            return 'The cells amount of first cage is less.'

    def __mul__(self, other):
        res_cell = self.cell * other.cell
        return res_cell

    def __truediv__(self, other):
        if self.cell > other.cell:
            res_cell = self.cell // other.cell
            return res_cell
        else:
            return 'The cells amount of first cage is less.'

    def make_order(self):
        while self.cell > self.cell_per_line:
            self.cell -= self.cell_per_line
            print('*' * self.cell_per_line, end='m')
        print('*' * self.cell)


cage1 = Cage(32, 5)
cage2 = Cage(18, 7)

cage3 = cage1 + cage2
print(cage3)

cage3 = cage1 - cage2
print(cage3)

cage3 = cage1 / cage2
print(cage3)

cage3 = cage1 * cage2
print(cage3)

cage1.make_order()
cage2.make_order()
