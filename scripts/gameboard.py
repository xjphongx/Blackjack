import pygame
from scripts.ring import Ring
from scripts.bet_menu import Bet_Menu
from scripts.cursor import Cursor
from scripts.player import Dealer
from scripts.ring_row import Ring_Row
from scripts.stack import DeckPile, DiscardPile
from scripts.state import State
from scripts.button import Button

class Gameboard(State):
    def __init__(self, game):
        super().__init__(game)
        #instantiating gameboard objects
        back_image = pygame.image.load("images/buttons/back_button.png").convert_alpha()
        self.back_button = Button(325, 50, back_image, self.game.IMAGE_SCALE)
        self.dealer = Dealer()
        self.deck_pile = DeckPile()
        self.deck_pile.load_cards_to_deck()
        self.discard_pile = DiscardPile()
        for i in range(8):     #shuffle the deck when starting the gameboard
            self.deck_pile.cut_deck()
            self.deck_pile.casino_shuffle()
        #clickable hand images and curved placement       
        hand_ring_image = pygame.image.load("images/hand_ring.png").convert_alpha()

        self.hand_2_x, self.hand_2_y = 900, 685
        self.hand_2_button = Button(self.hand_2_x,self.hand_2_y,hand_ring_image, scale=.25)
        self.hand_3_x, self.hand_3_y = 650, 700 #center
        self.hand_3_button = Button(self.hand_3_x,self.hand_3_y,hand_ring_image, scale=.25)
        self.hand_4_x, self.hand_4_y = 400, 685
        self.hand_4_button = Button(self.hand_4_x,self.hand_4_y, hand_ring_image, scale=.25)
        self.hand_5_x, self.hand_5_y = 150, 645
        self.hand_5_button = Button(self.hand_5_x,self.hand_5_y, hand_ring_image, scale=.25)
        confirm_button_image = pygame.image.load("images/buttons/confirm_button.png").convert_alpha()
        self.confirm_button = Button(self.game.display_width/2, self.game.display_height/2, confirm_button_image,scale=.1)
        #intialize ring row
        self.ring_row = Ring_Row(self.game, self)
        #intialize bet menu
        self.bet_menu = Bet_Menu(self.game, self)
        #intialize cursor object 
        self.cursor = Cursor(self.game) 

        #turn list
        self.turn_list = []
        
    def render(self,display):
        display.fill(self.game.background_color)
        #set up dealer
        self.game.draw_text("Dealer", 30, self.game.display_width/2,125)
        self.game.display.blit(self.dealer.dealer_image_surface, self.dealer.rect)           
        #set up deck
        self.game.display.blit(self.deck_pile.deck_back_image_surface, self.deck_pile.rect) 
        #set up discard pile
        self.game.display.blit(self.discard_pile.discard_pile_image_surface, self.discard_pile.rect)
        #self.game.draw_text('Playing game', 100, self.game.display_width/2,self.game.display_height/10)            
        self.game.draw_text("How many hands are you playing?", 50, self.game.display_width/2,self.game.display_height/5)
        #betting bar and functionality
        self.bet_menu.display()

        #hand ring functionality
        self.ring_row.display()

        if self.confirm_button.draw(self.game.display): #figure out how to clear this button
            if self.confirm_button.isActive == False:
                #combine the player and dealer hands, player goes first
                self.turn_list.extend(self.dealer.hand_list)
                self.turn_list.extend(self.game.player.hand_list)
                self.confirm_button.isActive = True
                #self.game.display.blit(self.hand_1_button.image,(self.confirm_button.rect.x,self.confirm_button.rect.y))
                print(f"Player's Hand {self.game.player.hand_list}")
                print(f"Dealer's Hand {self.dealer.hand_list}")
                print(f"Turn list {self.turn_list}")

                #TODO pass out cards at the respective locations




        #render the clickable button
        if self.back_button.draw(self.game.display):
            self.game.actions["back"] = True




    def update(self,actions):
        if actions["back"]:
            self.exit_state()
        self.game.reset_actions()