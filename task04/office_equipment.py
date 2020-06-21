import random


class OfficeEquipment:
    _instances = []

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.serial_number = random.randint(1000000000, 9999999999)
        self.status = 'NEW'
        self._instances.append(self)

    def __str__(self):
        return f'{self.brand} {self.model}, SN {self.serial_number}, {self.status}'

    def set_in_use_status(self):
        self.status = 'IN USE'

    def set_broken_status(self):
        self.status = 'BROKEN'

    @classmethod
    def instances(cls):
        return cls._instances


class Printer(OfficeEquipment):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self._ink_level = {
            'black': 0,
            'yellow': 0,
            'magenta': 0,
            'cyan': 0
        }
        self._ink_status = 'EMPTY'

    def print(self, numbers_of_page):
        for _ in range(numbers_of_page):
            if self._ink_status == 'EMPTY':
                print('WARNING! INK TANK IS EMPTY, PLEASE REFILL! PRINTING WAS STOPPED!')
                return
            if self._ink_status == 'LOW':
                print('WARNING! INK TANK IS LOW!')
            for color in self._ink_level:
                self._ink_level[color] -= random.randint(1, 10) / 10
            self.__update_ink_status()

    def ink_refill(self):
        for color in self._ink_level:
            self._ink_level[color] = 100
        self._ink_status = 'FULL'

    def __update_ink_status(self):
        min_value = min(self._ink_level.items(), key=lambda x: x[1])[1]

        if 21.0 < min_value < 95:
            self._ink_status = 'NORMAL'
        elif 3 < min_value < 20:
            self._ink_status = 'LOW'
        elif min_value < 3:
            self._ink_status = 'EMPTY'

    @property
    def ink_level(self):
        sign = 1
        black = round(self._ink_level['black'], sign)
        cyan = round(self._ink_level['cyan'], sign)
        magenta = round(self._ink_level['magenta'], sign)
        yellow = round(self._ink_level['yellow'], sign)

        return f'Ink level: black - {black}%, cyan - {cyan}%,' \
               f'yellow - {yellow}%, magenta - {magenta}%'


class Xerox(OfficeEquipment):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self._toner_level = 0
        self._toner_status = 'EMPTY'

    def print(self, numbers_of_page):
        for _ in range(numbers_of_page):
            if self._toner_status == 'EMPTY':
                print('WARNING! TONER TANK IS EMPTY, PLEASE REFILL! PRINTING WAS STOPPED!')
                return
            if self._toner_status == 'LOW':
                print('WARNING! TONER TANK IS LOW!')
            self._toner_level -= random.randint(1, 10) / 30
            self.__update_toner_status()

    def toner_refill(self):
        self._toner_level = 100
        self._toner_status = 'FULL'

    def __update_toner_status(self):

        if 21 < self._toner_level < 95:
            self._toner_status = 'NORMAL'
        if 3 < self._toner_level < 20:
            self._toner_status = 'LOW'
        elif self._toner_level < 3:
            self._toner_status = 'EMPTY'

    @property
    def toner_level(self):
        sign = 1
        toner_level = round(self._toner_level, sign)

        return f'Toner level: {toner_level}%.'


class Scanner(OfficeEquipment):
    pass


class Desktop(OfficeEquipment):
    pass


class Monitor(OfficeEquipment):
    pass
