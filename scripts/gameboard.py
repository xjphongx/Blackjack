import pygame
from scripts.player import Dealer
from scripts.stack import DeckPile, DiscardPile
from scripts.state import State
from scripts.button import Button

class Gameboard(State):
    def __init__(self, game):
        super().__init__(game)
        self.back_x = 150
        self.back_y = 500
        back_image = pygame.image.load("images/buttons/back_button.png").convert_alpha()
        self.back_button = Button(self.back_x, self.back_y, back_image, .10)
        self.dealer = Dealer()
        self.deck_pile = DeckPile()
        self.deck_pile.load_cards_to_deck()
        self.discard_pile = DiscardPile()
        for i in range(10):     #shuffle the deck when starting the gameboard
            self.deck_pile.cut_deck()
            self.deck_pile.casino_shuffle()
        #Set up player input variables
        self.input_font = pygame.font.Font(None,32)
        self.user_text = 'test' #recieve player input
        self.user_textbox_x = 150
        self.user_textbox_y = 40
        self.user_text_rect = pygame.Rect(self.game.display_width/2, 
                                        self.game.display_height/3,
                                        self.user_textbox_x,
                                        self.user_textbox_y)
        self.color = pygame.Color((255,255,255))

    def update(self,actions):
        pass

    def render(self,display):
        display.fill(self.game.background_color)