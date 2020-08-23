import hand
from combination_type import combination_type

create_card_list = hand.card.create_card(5)
hand.card.show_list(create_card_list)

a = combination_type(create_card_list)

# if hand.card.find_card(create_card_list, 1):
#     print('include A')
# else:
#     print('no A')

# b = hand.card.list_of_card_number(create_card_list)
# print(b)

#
x = a.is_straight()
print(x)