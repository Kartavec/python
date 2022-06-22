import re


def get_max_month_days(month):
    if month == 2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    return 31


class Date:
    def __init__(self, date_str):
        if self.validate(date_str):
            self.date = date_str
        else:
            raise ValueError

    def __str__(self):
        return self.date

    @classmethod
    def parse(cls, date_str):
        # return map(int, date_str.split('-'))
        date_split = date_str.split('-')
        return int(date_split[0]), int(date_split[1]), int(date_split[2])

    @staticmethod
    def validate(date_str):
        if not re.match(r'\d{1,2}-\d{1,2}-\d{4}', date_str):
            return False
        day, month, year = Date.parse(date_str)
        has_errors = month not in range(1, 12)
        has_errors |= day not in range(1, get_max_month_days(month))
        return not has_errors


try:
    print(Date.parse('46-4-2341'))
    print(Date.validate('46-4-2341'))
except ValueError:
    print('Date error')
