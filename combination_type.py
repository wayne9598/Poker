import hand


class combination_type:
    def __init__(self, five_cards:list):
        self.five_cards = five_cards

    def is_straight(self):
        x=0
        y = sorted(hand.card.list_of_card_number(self.five_cards))
        z = []

        for i in range(0, len(y)-1):
            if y[i+1] - y[i] == 1:
                x += 1

        if x == 4 or y.count(1) == 1 and y.count(10) == 1 and y.count(11) == 1 and y.count(12) == 1 and y.count(13) == 1:
            print('is straight')
            return True
        else:
            print('not straight')
            return False



