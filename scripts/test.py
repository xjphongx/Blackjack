from Hand import Hand
from Card import Card
from Stack import Stack

#testing adding Card objects to a Hand object
testCard1 = Card("Five",5,"Hearts")
testCard2 = Card("Jack",10,"Diamonds")
testCard3 = Card("King",10,"Spades")
testCard4 = Card("Three",3,"Clubs")

testHand = Hand()
testHand.add_card_to_hand(testCard1)
testHand.add_card_to_hand(testCard2)
testHand.add_card_to_hand(testCard3)
testHand.add_card_to_hand(testCard4)
print(f"Sum of Current Hand: {testHand.hand_sum}")
for i in range(testHand.hand_size):
    print(testHand.card_in_hand_list[i].get_card_type())

print("\ntesting removals below")
removed_card = testHand.remove_card_from_hand()
print(f"removed card: {removed_card.get_card_type()}")
testHand.update_hand()

print(f"Sum of test Hand after removal: {testHand.hand_sum}")
print(f"testHand")
for i in range(testHand.hand_size):
    print(testHand.card_in_hand_list[i].get_card_type())

#move the whole hand to a discard stack
print("\nMoving whole hand to discard")
discard_pile = Stack()
discard_pile.stack.extend(testHand.card_in_hand_list)
testHand.card_in_hand_list.clear()
testHand.reset_hand_sum()
testHand.update_hand()
print(f"Discard pile container: {discard_pile.show()}")
print(f"test hand container: {testHand.card_in_hand_list}")
#ending notes: discard stack extends testhand stack and update hand
#nothin in testHand after extend

print(f"Sum of test Hand: {testHand.hand_sum}")
for i in range(testHand.hand_size):
    print(testHand.card_in_hand_list[i].get_card_type())







    