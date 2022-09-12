from scripts.player import Dealer,Player
from scripts.stack import Deck

## game board will have the deal and all the players
## contain a stack of cards 

class GameBoard():
    def __init__(self):
        print("game board started")
        self.dealer = Dealer()
        self.deck = Deck()

    #load json png cards into the deck
    def load_cards_to_deck(self):
        pass

    def play(self):
        #play the game
        print("playing game")
        
        #set up deck 
        
        #set up discard pile

        #set up player 
            #set up player's hands

        #start turn system
        

    
###Testing down here

        

