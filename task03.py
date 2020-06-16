class CellRequiredError(Exception):
    pass


class MathActionError(Exception):
    pass


class WrongArgumentError(Exception):
    pass


def check_other_cell(other_cell):
    if not isinstance(other_cell, Cell):
        raise CellRequiredError('Математические действия возможны только между клетками')


def check_cell_argument(argument):
    if not (isinstance(argument, int) and argument > 0):
        raise WrongArgumentError('Для создания клетки аргумент должен быть положительным целым числом')


class Cell:
    def __init__(self, cell_size):
        check_cell_argument(cell_size)
        self.size = cell_size

    def __str__(self):
        return f'Количество ячеек - {self.size}'

    def __add__(self, other):
        check_other_cell(other)
        new_cell_size = self.size + other.size
        return Cell(new_cell_size)

    def __sub__(self, other):
        check_other_cell(other)
        if self.size > other.size:
            new_cell_size = self.size - other.size
            return Cell(new_cell_size)
        else:
            raise MathActionError('Разность количества ячеек двух клеток больше нуля')

    def __mul__(self, other):
        check_other_cell(other)
        new_cell_size = self.size * other.size
        return Cell(new_cell_size)

    def __truediv__(self, other):
        check_other_cell(other)
        new_cell_size = round(self.size / other.size)
        if new_cell_size == 0:
            raise WrongArgumentError('Величина новой клетки не может быть равна 0')
        return Cell(new_cell_size)

    def make_order(self, row_size):
        rows = self.size // row_size
        remainder = self.size % row_size
        result = ''
        for _ in range(rows):
            result += '*' * row_size
            result += '\n'
        result += '*' * remainder
        return result


if __name__ == '__main__':
    cell_1 = Cell(10)
    cell_2 = Cell(2)
    print(cell_1)
    print(cell_2)

    print('***СЛОЖЕНИЕ***')
    add_cell = cell_1 + cell_2
    print(add_cell)
    print()

    print('***ВЫЧИТАНИЕ***')
    sub_cell = cell_1 - cell_2
    print(sub_cell)
    print()

    print('***УМНОЖЕНИЕ***')
    mult_cell = cell_2 * cell_1
    print(mult_cell)
    print()

    print('***ДЕЛЕНИЕ***')
    div_cell = cell_1 / cell_2
    print(div_cell)
    print()

    print('***ПОРЯДОК***')
    order_cell = Cell(120)
    print(order_cell.make_order(11))

    # Расскоментируйте одну из строк, чтобы вызвать ошибку
    # error_cell = Cell('asd')
    # error_cell = cell_2 - cell_1
    # error_cell = cell_2 + 2
    # error_cell = Cell(-20)
    # error_cell = Cell(2) / Cell(100)