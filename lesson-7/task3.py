class CellSubException(Exception):
    pass


class CellTruedivException(Exception):
    pass


class Cell:
    def __init__(self, count: int):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count < other.count:
            raise CellSubException('sub error')
        return Cell(self.count - other.count)

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        if other.count == 0:
            raise CellTruedivException('division by zero')
        if self.count // other.count == 0:
            raise CellTruedivException('zero result')
        return Cell(self.count // other.count)

    def make_order(self, in_row: int):
        for i in range(self.count):
            print('*', end='')
            if (i+1) % in_row == 0:
                print('')
        print('')


c1 = Cell(20)
c2 = Cell(8)

print('SUM:', c1 + c2)
print('SUB:', c1 - c2)
print('MUL:', c1 * c2)
print('TRUEDIV:', c1 / c2)

c1.make_order(4)
