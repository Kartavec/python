import re


class InvalidListValueException(Exception):
    pass


class IntList:
    def __init__(self):
        self._elements = []

    @staticmethod
    def validate(value):
        return re.match(r'\d+', value)

    def append(self, value):
        if not self.validate(value):
            raise InvalidListValueException('Input value must be number')
        self._elements.append(int(value))

    def __str__(self):
        return ' '.join(map(str, self._elements))


int_list = IntList()
while True:
    input_string = input('Enter number or stop: ')
    if input_string.lower() == 'stop':
        break

    try:
        int_list.append(input_string)
    except InvalidListValueException as e:
        print(e.__class__.__name__, ':', e)

print('Result:')
print(int_list)
