import sys


def check_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def check_days(days, month, year):
    months_30_days = [4, 6, 9, 11]
    months_31_days = [1, 3, 5, 7, 8, 10, 12]

    if month in months_30_days and days in range(1, 31):
        return True

    if month in months_31_days and days in range(1, 32):
        return True

    if month == 2 and (check_leap_year(year) and days in range(1, 30)):
        return True

    if month == 2 and (not check_leap_year(year) and days in range(1, 29)):
        return True

    return False


def check_month(month):
    return month in range(1, 13)


class Date:
    days = 0
    months = 0
    years = 0

    def __init__(self, raw_date):
        self.raw_date = raw_date

    @staticmethod
    def validate_date(date):
        days, months, years = Date.parse_date(date)

        if check_days(days, months, years) and check_month(months):
            return True

        return False

    @classmethod
    def parse_date(cls, date):

        try:
            days, months, years = date.split('-')
            return int(days), int(months), int(years)
        except (TypeError, ValueError) as error:
            print(f"Couldn't parse date: {error}")
            sys.exit()


if __name__ == '__main__':
    print(Date.parse_date('25-12-2020'))
    print(Date.parse_date('33-22-0000'))
    print()
    print(Date.validate_date('25-12-2020'))
    print(Date.validate_date('33-22-0000'))
    print()
    print(Date.validate_date('28-02-2020'))
    print(Date.validate_date('29-02-2020'))
    print(Date.validate_date('30-02-2020'))
    print()
    print(Date.validate_date('12-may-2020'))
    print(Date.validate_date('12/11'))