import pygame
from scripts.player import Dealer,Player
from scripts.stack import Deck

## game board will have the deal and all the players
## contain a stack of cards 

class GameBoard():
    def __init__(self,game):
        print("game board started")
        self.game = game
        self.dealer = Dealer()
        self.deck = Deck()


    #load json png cards into the deck
    def load_cards_to_deck(self):
        pass

    def display_gameboard(self):
        #set up dealer
        self.game.screen.blit(self.game.gameboard.dealer.dealer_image_surface,self.game.gameboard.dealer.rect)           
        #set up deck 
        #set up discard pile
        #set up player 
            #set up player's hands
        #start turn system
        
        
    def check_input(self):
        pass
    


        

