class Matrix:
    def __init__(self, list1, list2, list3):
        self.list1 = list1
        self.list2 = list2
        self.list3 = list3

    def __str__(self):
        return f'{self.list1}\n{self.list2}\n{self.list3}\n'

    def __add__(self, other):
        list7 = []
        list8 = []
        list9 = []
        for i in range(0, 3):
            line1 = self.list1[i] + other.list1[i]
            list7.append(line1)
        for i in range(0, 3):
            line2 = self.list2[i] + other.list2[i]
            list8.append(line2)
        for i in range(0, 3):
            line3 = self.list3[i] + other.list3[i]
            list9.append(line3)
        res = f'NEW MATRIX\n{list7}\n{list8}\n{list9}'
        return res


list1 = [1, 3, 6]
list2 = [2, 5, 7]
list3 = [0, 4, 9]
list4 = [6, 6, 9]
list5 = [2, 2, 4]
list6 = [9, 2, 7]

matrix1 = Matrix(list1, list2, list3)
matrix2 = Matrix(list4, list5, list6)
print(matrix1.__str__())
print(matrix2.__str__())

matrix3 = matrix1 + matrix2
print(matrix3)
