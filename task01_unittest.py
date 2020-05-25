import unittest
import task01


class MyTestCase(unittest.TestCase):
    def test_division(self):
        self.assertEqual(task01.division(4, 2), 2)

    def test_zero_division(self):
        self.assertEqual(task01.division(4, 0), None)
        with self.assertRaises(TypeError):
            task01.division('foo', 'buzz')

    def test_number_convert_to_int(self):
        self.assertEqual(task01.convert_to_int('6'), 6)

    def test_string_convert_to_int(self):
        self.assertEqual(task01.convert_to_int('example'), None)


if __name__ == '__main__':
    unittest.main()
