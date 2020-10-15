class Matrix:
    def __init__(self, elems):
        self.matrix = elems
        self.height = len(elems)
        self.width = len(elems[0])

    def __add__(self, other):
        if self.height != other.height:
            raise TypeError('Different matrix heights!')
        if self.height != other.height:
            raise TypeError('Different matrix widths!')
        ret_matrix = []
        for row1, row2 in zip(self.matrix, other.matrix):
            ret_matrix.append([x + y for x, y in zip(row1, row2)])
        return Matrix(ret_matrix)

    def __str__(self):
        ret_str = ''
        for row in self.matrix:
            ret_str = ret_str + f'{row}' + '\n'
        return ret_str


a = Matrix([[1, 2],
            [5, 6]])

b = Matrix([[3, 4],
            [7, 8]])

print((a + b))
