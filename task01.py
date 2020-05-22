def get_type(var):
    return type(var)


if __name__ == '__main__':
    different_data = [5,
                      'hello world',
                      ['winter', 'spring', 'summer', 'fall'],
                      (4, 8, 15, 16, 23, 42),
                      set('bugaga'),
                      {'01': 'January',
                       '02': 'February',
                       '03': 'March',
                       '04': 'April',
                       '05': 'May',
                       '06': 'June',
                       '07': 'July',
                       '08': 'August',
                       '09': 'September',
                       '10': 'October',
                       '11': 'November',
                       '12': 'December'},
                      True,
                      b'python',
                      None,
                      Exception('Error')]

    for data in different_data:
        print(f'Data is {data}')
        data_type = get_type(data)
        print(f'Type of data is {data_type}')
        print()
