import random

from hand import pack_of_card

class deal:
    def __init__(self, x:pack_of_card):
        self.flop_list = []
        self.turn_list = []
        self.river_list = []
        self.x = x

    def flop(self):
        for i in range(3):
            n = random.randint(0,len(self.x.card_list)-1)
            self.flop_list.append(self.x.card_list[n])
            self.x.remove_card(self.x.card_list[n])
        return self.flop_list

    def show_flop(self, new_line:bool = False):
        print('Flop: ', end='')
        for i in self.flop_list:
            i.show_card()
        if new_line:
            print()

    def turn(self):
        # for i in self.x.card_list:
        #     i.show_card
        for i in range(1):
            n = random.randint(0,len(self.x.card_list)-1)
            self.turn_list.append(self.x.card_list[n])
            self.x.remove_card(self.x.card_list[n])
        return self.turn_list

    def show_turn(self, new_line:bool = False):
        print('Turn: ', end='')
        for i in self.turn_list:
            i.show_card()
        if new_line:
            print()

    def river(self):
        for i in range(1):
            n = random.randint(0,len(self.x.card_list)-1)
            self.river_list.append(self.x.card_list[n])
            self.x.remove_card(self.x.card_list[n])
        return self.river_list

    def show_river(self, new_line:bool=False):
        print('River: ',end='')
        for i in self.river_list:
            i.show_card()
        if new_line:
            print()