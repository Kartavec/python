import random

CARD_WIDTH = 9
CARD_ROWS = 3
LOTO_MAX_NUMBER = 90


def barrels_sack(max_num):
    barrels = random.sample(range(1, max_num + 1), max_num)
    while len(barrels):
        yield barrels.pop()


class Game:
    def __init__(self, rows, width, loto_max_number):
        self.player_card = Card(rows, width, loto_max_number)
        self.pc_card = Card(rows, width, loto_max_number)
        self.sack = barrels_sack(loto_max_number)

    def start(self):
        while True:
            print('Карточка компьютера')
            print(self.pc_card)
            print('Ваша карточка')
            print(self.player_card)
            next_number = next(self.sack)
            print(f'Новый бочоночек под номером {next_number}!')
            user_decision = input('Вычёркиваем? (y, n)')
            if user_decision == 'y':
                result = self.player_card.cross_num_out(next_number)
                if result:
                    print('Номер есть в карте, вычёркиваем его и продолжаем')
                    if self.player_card.nums_left == 0:
                        print('Поздравляю вы вычеркнули все номера и выйграли!')
                        return True
                    print(f'Осталось вычеркнуть {self.player_card.nums_left} номеров')

                else:
                    print('Номера нет в карте, вы проиграли')
                    return False
            else:
                result = self.player_card.is_number_in_card(next_number)
                if result:
                    print('Номер есть в карте, но вы его не вычеркнули, вы проиграли')
                    return False

            self.pc_card.cross_num_out(next_number)
            if self.pc_card.nums_left == 0:
                print('Компьютер всё вычеркнул, вы проиграли')
                return False
        return True


class Card:
    def __init__(self, rows, width, loto_max_number):
        """Создаем мешок с бочонками и выставляем их на случайные номера в рядах карты
        В списке self.loto_max_number лежат списки по рядам с номерами карточки,
        Номер карточки представлен списком
        """
        sack = barrels_sack(loto_max_number)
        self.rows = rows
        self.width = width
        self.loto_max_number = loto_max_number
        self.nums_left = rows * 5
        self.numbers_in_card = []
        for row in range(rows):
            positions = random.sample(range(width), 5)
            positions.sort()
            for pos in positions:
                num = Number(next(sack), [row, pos])
                self.numbers_in_card.append(num)

    def __str__(self):
        ret_str = '----------------------------\n'
        for row in range(self.rows):
            for line in range(self.width):
                pos = [row, line]
                for num in self.numbers_in_card:
                    if num.pos == pos:
                        if num.crossed:
                            ret_str += '-  '
                            break
                        else:
                            if num.value > 9:
                                ret_str += f'{num.value} '
                            else:
                                ret_str += f'{num.value}  '
                            break
                else:
                    ret_str += '   '
            ret_str += '\n'
        ret_str += '----------------------------\n'
        return ret_str

    def cross_num_out(self, value):
        for num in self.numbers_in_card:
            if num.value == value:
                self.nums_left -= 1
                num.crossed = True
                return True
        return False

    def is_number_in_card(self, value):
        for num in self.numbers_in_card:
            if num.value == value and not num.crossed:
                return True
        return False


class Number:
    def __init__(self, value, pos):
        self.value = value
        self.pos = pos
        self.crossed = False


game = Game(3, 9, 90)

game.start()
