import pygame,json
from scripts.player import Dealer,Player
from scripts.stack import DeckPile, DiscardPile
from scripts.card import Card

## game board will have the deal and all the players
## contain a stack of cards 

class GameBoard():
    def __init__(self,game):
        print("game board started")
        self.game = game
        self.dealer = Dealer()
        self.deck_pile = DeckPile()
        self.deck_pile.load_cards_to_deck()
        self.discard_pile = DiscardPile()

        
        
    def check_input(self):
        pass
    


        

