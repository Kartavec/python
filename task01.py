def check_matrix(matrix):
    if type(matrix) != list:
        print('Argument is not list!')
        return False

    for nested_list in matrix:
        if type(nested_list) != list:
            print('Nested elements must be list!')
            return False

    row_size = len(matrix[0])

    for nested_list in matrix:
        if len(nested_list) != row_size:
            print('Nested elements must have equal size!')
            return False

    return True


def get_matrix_size(matrix):
    height = len(matrix)
    width = len(matrix[0])
    return {'height': height,
            'width': width}


def get_matrix_sum(first_m, second_m):
    result = []
    for i in range(len(first_m)):
        result.append([])
        for j in range(len(first_m[0])):
            result[i].append(first_m[i][j] + second_m[i][j])

    return result


def check_equal_of_matrices_sizes(first_m, second_m):
    first_m_size = get_matrix_size(first_m)
    second_m = get_matrix_size(second_m)
    return first_m_size == second_m


class Matrix:
    def __init__(self, matrix):
        if check_matrix(matrix):
            self.matrix = matrix
        else:
            raise ValueError("Cann't create matrix with wrong argument!")

    def __str__(self):
        result = ''
        for row in self.matrix:
            result += ' '.join(str(x) for x in row)
            result += '\n'
        return result

    def __add__(self, other_matrix):
        if check_matrix(other_matrix) and check_equal_of_matrices_sizes(self.matrix, other_matrix):
            self.matrix = get_matrix_sum(self.matrix, other_matrix)
        else:
            raise ValueError("Cann't sum matrices!")


if __name__ == '__main__':

    test = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    other = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]

    right_other = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1],
    ]

    dict_matrix = {'1': 1, '2': 2, '3': 3}

    matrix_with_nested_tuple = [
        [9, 8, 7],
        [6, 5, 4],
        (3, 2, 1),
    ]

    non_matrix_list = [
        [1, 2, 3],
        [4], [5],
        [6], [7], [8], [9]
    ]

    my_matrix = Matrix(test)

    print(my_matrix)

    my_matrix + right_other
    print(my_matrix)
    my_matrix + right_other
    my_matrix + right_other
    print(my_matrix)

    # Раскомментируйте одну из строк, чтобы вызвать ошибки
    # print(my_matrix + other)
    # print(my_matrix + dict_matrix)
    # print(my_matrix + matrix_with_nested_tuple)
    # another_matrix = Matrix(non_matrix_list)