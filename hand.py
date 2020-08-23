import random

from utility import check


class card:
    def __init__(self, color, number):
        if number < 1 or number > 14:
            print('Your', number, 'Number should be between 1-13')
        else:
            self.number = number

        if color < 1 or color > 4:
            print('Your', color, 'Number should be between 1-3')
        else:
            self.color = color

    def __eq__(self, other):
        return self.number == other.number and self.color == other.color

    def __sub__(self, other):
        return self.number - other.number

    # def __lt__(a, b):
    # def __le__(a, b):
    # def __ne__(a, b):
    # def __ge__(a, b):
    # def __gt__(a, b):

    def show_color(self):
        if self.color == 4:
            print('\u2660', end='')
        elif self.color == 3:
            print('\u2665', end='')
        elif self.color == 2:
            print('\u2666', end='')
        elif self.color == 1:
            print('\u2663', end='')

    def show_number(self):
        a = ['A', 'J', 'Q', 'K']
        b = [1, 11, 12, 13]
        if self.number in b:
            print(a[b.index(self.number)], end=' ')
        else:
            print(self.number, end=' ')

    def show_card(self):
        self.show_color()
        self.show_number()

    @staticmethod
    def create_card(number_of_card):
        create_card_list = []
        for i in range(number_of_card):
            color = input('Card color= ')
            number = input('Card number= ')
            create_card_list.append(card(int(color), int(number)))
        return create_card_list

    @staticmethod
    def show_list(a: list):
        for i in a:
            i.show_card()

    @staticmethod
    def find_card(a: list, number):
        for i in a:
            if i.number == number:
                return True

    @staticmethod
    def list_of_card_number(a: list):
        b = []
        for i in a:
            b.append(i.number)
        return b
    # def find_card(self, a, number):
    #     for i in a:
    #         if self.number == number:
    #             return True



class pack_of_card:
    def __init__(self):
        self.card_list = []
        for j in range(1, 5):
            for i in range(1, 14):
                one_card = card(j, i)
                self.card_list.append(one_card)

    def show_pack_of_card(self):
        for i in self.card_list:
            i.show_card()

    def remove_card(self, card):
        return self.card_list.remove(card)


class UI:
    @staticmethod
    def input_my_hand():

        while True:
            card1_color = input('Enter card1 color (1 = ♣, 2 = ♦, 3 = ♥, 4 = ♠): ')
            card1_number = input('Enter card1 number: ')
            card2_color = input('Enter card1 color (1 = ♣, 2 = ♦, 3 = ♥, 4 = ♠): ')
            card2_number = input('Enter card1 number: ')

            if card1_color == card2_color and card1_number == card2_number:
                print('Card1 and Card2 should be different!')
                continue

            a = check.check_card(card1_color, 1, 4)
            b = check.check_card(card1_number, 1, 13)
            c = check.check_card(card2_color, 1, 4)
            d = check.check_card(card2_number, 1, 13)

            if a and b and c and d:
                break
            else:
                print('Input not in range')
                continue

        return card(int(card1_color), int(card1_number)), card(int(card2_color), int(card2_number))


class myhand:
    def __init__(self, card1: card, card2: card):
        self.card1 = card1
        self.card2 = card2

    def myhand_list(self):
        my_hand_list = [self.card1, self.card2]
        return my_hand_list

    def show_my_hand(self, new_line: bool = False):
        print('My Hand: ', end='')
        self.card1.show_card()
        self.card2.show_card()
        if new_line:
            print()


def combination(a: list, b: list, c: list, d: list):
    e = a + b + c + d
    print('Combination: ', end='')
    for i in e:
        i.show_card()
    return e

#
# def find_all_combination(a: list):
#     all_comb = []
#     b = []
#     for i in range(6):
#         for x in range(i,5):
#             c = a.remove(a[i])
#             print('c: ', c)
#             b.append(c)
#     print('all comb: ', b)




