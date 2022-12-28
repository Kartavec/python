"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, *matr):
        self.matr = matr
        print(f'{self.matr} введенные данные имеют тип: {type(self.matr)}')

    def __str__(self):
        out_put = ''
        for el in self.matr:
            el = str(el)
            el = el.replace(',', '').replace(']', '').replace('[', '')
            out_put = out_put + '\n' + el
        return out_put



    def __add__(self, other):
        if len(self.matr) != len(other.matr):       #проверяем возможность сложения матиц
            print('матрицы не равны по количеству строк. сложение не возможно!')
        for row_elem in range(len(self.matr)):
            if len(self.matr[row_elem]) != len(other.matr[row_elem]):
                print('матрицы не равны по количеству столбцов. сложение не возможно!')
                break
        sum_matrix = self.matr
        for row in range(len(self.matr)):
            for column in range(len(self.matr[row])):
                sum_matrix[row][column] = self.matr[row][column] + other.matr[row][column]
        return sum_matrix


matrix_1 = Matrix([1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1])   #подумал, что кортеж списков будет работать
print(matrix_1)                                               #быстрее списка списков

matrix_2 = Matrix([2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2])
print(matrix_2)

matrix_sum = matrix_1 + matrix_2
print(type(matrix_sum))
print(f'сумма двух матриц {matrix_sum}')


print('------------------------------------------------------------------------------------------')

"""2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность 
(класс) этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом 
проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) 
и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), 
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
реализовать абстрактные классы для основных классов проекта, проверить на практике работу 
декоратора @property.
"""

from abc import ABC, abstractmethod

class Roba:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabrik_spend(self):
        pass

    def __add__(self, other):
        total_spend = self.spend + other.spend
        return total_spend

class Coat(Roba):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def fabrik_spend(self):
        self.spend = self.size / 6.5 + 0.5
        return self.spend


class Suit(Roba):
    def __init__(self, name, heigh):
        super().__init__(name)
        self.heigh = heigh

    @property
    def fabrik_spend(self):
        self.spend = self.heigh * 2 + 0.3
        return self.spend


coat_1 = Coat('coat #1', 56)

print(f'расход ткани на пальто {coat_1.fabrik_spend:.2f}')

suit_1 = Suit('suit #1', 1.8)

print(f'расход ткани на костюм {suit_1.fabrik_spend:.2f}')

print(f'общий расход ткани составил {coat_1 + suit_1:.2f}')

print('------------------------------------------------------------------------------------------')


"""3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо 
создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству 
ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки арифметических 
операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), 
деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять увеличение, 
уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек 
исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества 
ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.

Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение 
количества ячеек этих двух клеток.

Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное 
деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество 
ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно 
переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются 
все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. 
Тогда метод make_order() вернёт строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. 
Тогда метод make_order() вернёт строку: *****\n*****\n*****."""

class Cell:
    def __init__(self, quantity, grid):
        if type(quantity) == int:
            self.quantity = quantity
        else:
            print('Количество ячеек в клетке должно быть целым числом')
        self.grid = grid


    def __add__(self, other):
        total_quantity = self.quantity + other.quantity
        return total_quantity


    def __mul__(self, other):
        total_quantity = self.quantity * other.quantity
        return total_quantity

    def __sub__(self, other):
        if self.quantity < other.quantity:
            print('Количество ячеек в клетке слева недостаточно для вычитания')
        else:
            total_quantity = self.quantity - other.quantity
            return total_quantity


    def __truediv__(self, other):
        total_quantity = self.quantity // other.quantity
        return total_quantity


    def make_order(self):
        for elem in range(self.quantity // self.grid):
            print('*' * self.grid)
        print('*' * (self.quantity % self.grid))
        print('-' * self.grid)      #линия для наглядности разделения


cell_1 = Cell(6, 5)
cell_2 = Cell(8, 7)

result_cell = cell_1 + cell_2
print(result_cell)

result_cell = cell_1 - cell_2
print(result_cell)

result_cell = cell_1 * cell_2
print(result_cell)

result_cell = cell_1 / cell_2
print(result_cell)

cell_1.make_order()
cell_2.make_order()
