from player import Dealer
from stack import Deck ## from Stack.py file, import and use the Stack class
from card import Card   ## from Card.py file, import and uses Card class


import pygame
import json 
import sys

pygame.init()
screen = pygame.display.set_mode((1300,900)) #final dimensions
pygame.display.set_caption('Test Window')
clock = pygame.time.Clock()

##Loading json object to Card object
testStack = Deck()
with open('cards.json') as jsonfile:
#jsonfile = open('cards.json')#another way to open
    card = json.load(jsonfile)
print(f"The is the amount of decks in this stack {card['amount_of_decks']}")
for data_item in card['card_decks']:
##create a new Card for every interation and push into stack
    card_Obj = Card(data_item['card_type'], data_item['pip_value'], data_item['suit'],data_item['card_image'])
    card_Obj.card_image_surface = pygame.transform.rotozoom(card_Obj.card_image_surface,0,.2) #makes the cards smaller
    testStack.push(card_Obj)
jsonfile.close()


print("Updating stack size")
testStack.update_size()

print("Stack before cut")
for i in range(testStack.get_size()):
    print(testStack.stack[i].card_type,end = " ")

print("Initializing cut()")
testStack.cut_deck()
#check out the shuffle cut list
for j in range(testStack.get_size()):
    print(testStack.stack[j].card_type, end = " ")

print("\nIntializing casino_shuffle()")
testStack.casino_shuffle()
testStack.cut_deck()
testStack.casino_shuffle()
testStack.casino_shuffle()
testStack.cut_deck()
testStack.casino_shuffle()
for j in range(testStack.get_size()):
    print(testStack.stack[j].card_type, end = " ")

#testing dealer
dealer = Dealer()

while True:
    #screen.blit(image surface, image rectangle)
    screen.fill((123,132,4))
    screen.blit(testStack.stack[-1].card_image_surface,testStack.stack[-1].rect )
    screen.blit(dealer.dealer_image_surface, dealer.rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    pygame.display.update()
    clock.tick(60)




