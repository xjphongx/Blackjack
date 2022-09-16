#test player and dealer on a board with gameboard instances
from turtle import end_fill
from scripts.player import Dealer,Player
from scripts.card import Card
from scripts.hand import Hand
import json


from scripts.stack import DeckPile, Stack

MINIMUM_BET = 50

#create gameboard objects below
dealer = Dealer()
deckpile = DeckPile()
discardpile = Stack()
player = Player()



#load json card objects into Card objects
CARD_PATH_TO_JSON = 'scripts/cards.json'
with open(CARD_PATH_TO_JSON) as jsonfile:
    cards = json.load(jsonfile)
for data_item in cards['card_decks']:
    #create a new card for every iteration
    card_object = Card(
        data_item['type'],
        data_item['pip_value'], 
        data_item['suit'],
        ) #data_item['card_image'] put this back in
        
    deckpile.push(card_object)

jsonfile.close()
print(deckpile.size)

#shuffle the deck
deckpile.cut_deck()
deckpile.casino_shuffle()
deckpile.cut_deck()
deckpile.casino_shuffle()
deckpile.cut_deck()
deckpile.casino_shuffle()
for i, card in enumerate(deckpile.stack):
    print(card.type, end= " ")

#Blackjack starts below
print("Welcome to the Black Jack Test")
print("Minimum bet is 50 coins per hand\n")
#get player input, how many hands do player want
print("How many hands are you playing?")
handAmount = int(input()) #raise exception error if out side of amount range
for i in range(handAmount):
    player.add_Hand()
    player.subtract_funds(MINIMUM_BET)

print(f"Current Player's funds: {player.fund}")
#place all active hands in a new list
turn_list = []
turn_list.extend(player.hand_list)
turn_list.extend(dealer.hand_list)
print(f"Turn List: {turn_list}")

#this is the passing out cards phase
for rotation in range(2): 
    #pass out one card to each hand
    #print(f"Rotation: {rotation}")#
    for i, hand in enumerate(turn_list):
        #pop top of deck stack and add to that specific hand
        #print(f"Iteration: {i} Hand: {hand}")
        topcard = deckpile.top() 
        deckpile.pop()
        #print(f"Top card of deck stack: {topcard.type}")
        #print(f"Hand: {hand} This is the real hand")
        hand.add_card(topcard)
#print(turn_list[0].card_list[0].type)


#This is looking at the cards phase
playingHandAmount = handAmount+1 #plus 1 for the dealers hand
#loop through all the hands
for i, hand in enumerate(turn_list):
    #loop through the cards in THAT specific hand
    print(f"Player {i}'s hand:", end = " ")
    for j, card in enumerate(hand.card_list):
        print(hand.card_list[j].type,end = " ")

    #if hand has an Ace card, show two different sum values
    if hand.hasAce:
        print(f"Hand Sum: {hand.hand_sum}")
        print(f"Upper Hand Sum: {hand.hand_upper_sum}")
    else:
        print(f"Hand Sum: {hand.hand_sum}")



        
        
#get the player action response
def get_player_action():
    #get the player's action input
    action = input("hit, stand, double, or split")
    if action == 'hit':
        #hit
        pass
    elif action == 'stand':
        #stand
        pass        
    elif action == 'split':
        pass
    elif action == 'double':
        pass 
    else:
        print("input error")



def hit():
    
    pass
        
        






