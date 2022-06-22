import unittest


class Complex:
    def __init__(self, real, imagine):
        assert isinstance(real, int)
        assert isinstance(imagine, int)
        self.real = real
        self.imagine = imagine

    def __add__(self, other):
        return Complex(self.real + other.real, self.imagine + other.imagine)

    def __mul__(self, other):
        return Complex(
            real=(self.real * other.real - self.imagine * other.imagine),
            imagine=(self.real * other.imagine + self.imagine * other.real)
        )

    def __str__(self):
        if self.imagine == 0:
            return str(self.real)

        return '(%s%s%sj)' % (
            self.real,
            '+' if self.imagine > 0 else '-',
            abs(self.imagine) if self.imagine != 1 else ''
        )


class ComplexTest(unittest.TestCase):
    def test_str(self):
        complex_1 = Complex(1, 2)
        complex_2 = complex(1, 2)
        self.assertEqual(str(complex_1), str(complex_2))

    def test_add(self):
        c_1_1 = Complex(1, 2)
        c_1_2 = Complex(2, 1)

        c_2_1 = complex(1, 2)
        c_2_2 = complex(2, 1)

        self.assertEqual(str(c_1_1 + c_1_2), str(c_2_1 + c_2_2))

    def test_mul(self):
        c_1_1 = Complex(3, 1)
        c_1_2 = Complex(8, 4)

        c_2_1 = complex(3, 1)
        c_2_2 = complex(8, 4)

        self.assertEqual(str(c_1_1 * c_1_2), str(c_2_1 * c_2_2))


unittest.main()
