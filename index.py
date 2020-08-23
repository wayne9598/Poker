import hand

# Create a pack of card
from deal import deal

b = hand.pack_of_card()
# b.show_pack_of_card()

# Input my hand
card1, card2 = hand.UI.input_my_hand()
c = hand.myhand(card1,card2)
my_hand_list = c.myhand_list()
c.show_my_hand(new_line = True)

# Remove hand from the pack of card
# b.remove_card(card1)
# b.remove_card(card2)
# b.show_pack_of_card()
#
# # Create my hand
# my_hand = hand.myhand(card1,card2)

# Flop
mid_card = deal(b)

flop = mid_card.flop()
mid_card.show_flop(new_line = True)

turn = mid_card.turn()
mid_card.show_turn(new_line = True)

river = mid_card.river()
mid_card.show_river(new_line = True)

combination = hand.combination(my_hand_list, flop, turn, river)

# hand.find_all_combination(combination)