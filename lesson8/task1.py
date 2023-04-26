class Data():

    @classmethod
    def data_int(cls, new_data):
        global day
        global month
        global year
        new_data = new_data.split('-')
        day = int(new_data[0])
        month = int(new_data[1])
        year = int(new_data[2])

    @staticmethod
    def validation (day, month):
        if day > 31 or day < 1 or month > 12 or month < 1:
            print('Your data is incorrect. Please, restart the program and \
enter new data.')
        else:
            print(f'The data is correct.\n{day}-{month}-{year}')


new_data = (input('Please, enter the data in format dd-mm-yy.\t'))
Data.data_int(new_data)
Data.validation(day, month)
