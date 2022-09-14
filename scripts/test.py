from hand import Hand
from card import Card
from stack import Stack
import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
display = pygame.Surface((500,500))
clock = pygame.time.Clock()

#testing adding Card objects to a Hand object
testCard1 = Card("Five",5,"Hearts","../images/PNG_cards/5_of_hearts.png")
testCard2 = Card("Jack",10,"Diamonds","../images/PNG_cards/jack_of_diamonds.png")
testCard3 = Card("King",10,"Spades","../images/PNG_cards/king_of_spades.png")
testCard4 = Card("Three",3,"Clubs","../images/PNG_cards/3_of_clubs.png")

testHand = Hand()
testHand.add_card(testCard1)
testHand.add_card(testCard2)
testHand.add_card(testCard3)
testHand.add_card(testCard4)
print(f"Sum of Current Hand: {testHand.hand_sum}")
for i in range(testHand.hand_size):
    print(testHand.card_list[i].card_type)

print("\ntesting removals below")
removed_card = testHand.remove_card_from_hand()
print(f"removed card: {removed_card.card_type}")
testHand.update_hand()

print(f"Sum of test Hand after removal: {testHand.hand_sum}")
print(f"testHand")
for i in range(testHand.hand_size):
    print(testHand.card_list[i].card_type)

#move the whole hand to a discard stack
print("\nMoving whole hand to discard")
discard_pile = Stack()
discard_pile.stack.extend(testHand.card_list)
testHand.card_list.clear()
testHand.reset_hand_sum()
testHand.update_hand()
print(f"Discard pile container: {discard_pile.show()}")
print(f"test hand container: {testHand.card_list}")
#ending notes: discard stack extends testhand stack and update hand
#nothin in testHand after extend

print(f"Sum of test Hand: {testHand.hand_sum}")
for i in range(testHand.hand_size):
    print(testHand.card_list[i].card_type)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(display,(0,0))
    pygame.display.update()
    clock.tick(60)





    