import random


class MatrixException(Exception):
    pass


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __str__(self):
        return "\n".join([' '.join(map(str, tmp)) for tmp in self.matrix])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise MatrixException('Matrices has different size')
        # res = [map(sum, zip(*tmp)) for tmp in zip(self.matrix, other.matrix)]
        res = generate_matrix(self.rows, self.cols, nulls=True)
        for i in range(self.rows):
            for j in range(self.cols):
                res[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(res)


def generate_matrix(rows: int, cols: int, *, nulls: bool = False) -> list:
    matrix = []
    for i in range(rows):
        matrix.append([random.randint(0, 100) if not nulls else 0 for j in range(cols)])
    return matrix


matrix1 = Matrix(generate_matrix(
    int(input('Enter rows matrix 1: ')),
    int(input('Enter cols matrix 1: ')),
))

matrix2 = Matrix(generate_matrix(
    int(input('Enter rows matrix 2: ')),
    int(input('Enter cols matrix 2: ')),
))

print('Matrix 1')
print(matrix1)
print('Matrix 2')
print(matrix2)
try:
    print('Matrix sum:')
    print(matrix1 + matrix2)
except MatrixException as e:
    print(e)
