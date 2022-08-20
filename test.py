from Hand import Hand
from Card import Card

#testing adding Card objects to a Hand object

testCard1 = Card("Five",5,"Hearts")
testCard2 = Card("Jack",10,"Diamonds")
testCard3 = Card("King",10,"Spades")
testCard4 = Card("Three",3,"Clubs")

testHand = Hand()
testHand.add_card_to_hand(testCard1)
testHand.add_cardpip_to_sum(testCard1.pip_value)
testHand.add_card_to_hand(testCard2)
testHand.add_cardpip_to_sum(testCard2.pip_value)
testHand.add_card_to_hand(testCard3)
testHand.add_cardpip_to_sum(testCard3.pip_value)
testHand.add_card_to_hand(testCard4)
testHand.add_cardpip_to_sum(testCard4.pip_value)
print(f"Sum of Current Hand: {testHand.hand_sum}")

for i in range(testHand.hand_size):
    print(testHand.card_in_hand_list[i].get_card_type())