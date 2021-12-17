# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class MyZeroDivisionError(Exception):
    def __init__(self, message="Деление на 0"):
        self.message = message
        super().__init__(self.message)

    # переопределяем метод '__str__'
    def __str__(self):
        return f'{self.message}'


while True:

    a = int(input('Введите делимое: '))
    b = int(input('Введите делтель: '))
    try:
        if b == 0:
            raise MyZeroDivisionError
        else:
            print(f'Результат деления {a} / {b} = {a/b:.2}')
    except MyZeroDivisionError as e:
        print(e.message)
        print('Повторите ввод... (-1 - выход')

