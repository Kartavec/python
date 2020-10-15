class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        dif = self.num - other.num
        if dif > 0:
            return Cell(dif)
        else:
            return None

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        div = self.num / other.num
        print(div)
        if div > 0:
            return Cell(int(div))
        else:
            return None

    def make_order(self, count_in_row):
        for i in range(1, self.num + 1):
            print('*', end='')
            if i % count_in_row == 0:
                print('')
        print('')

c1 = Cell(15)
c2 = Cell(8)
c3 = c1+c2
# c3.make_order(3)
# print(c3.num)
# (c3/c2).make_order(2)
с4 = c3*c2
с4.make_order(5)