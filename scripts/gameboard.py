import pygame
from scripts.player import Dealer
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
        hand_1_x, hand_1_y = 1150,760
        self.hand_1_button = Button(hand_1_x,hand_1_y,hand_ring_image, scale=.25)
        hand_2_x, hand_2_y = 900,785
        self.hand_2_button = Button(hand_2_x,hand_2_y,hand_ring_image, scale=.25)
        hand_3_x, hand_3_y = 650, 800 #center
        self.hand_3_button = Button(hand_3_x,hand_3_y,hand_ring_image, scale=.25)
        hand_4_x, hand_4_y = 400, 785
        self.hand_4_button = Button(hand_4_x,hand_4_y, hand_ring_image, scale=.25)
        hand_5_x, hand_5_y = 150, 760
        self.hand_5_button = Button(hand_5_x,hand_5_y, hand_ring_image, scale=.25)


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
        
        #TODO set up player input
        
        if self.hand_1_button.draw(self.game.display):
            if self.hand_1_button.isActive == False:
                self.game.player.add_Hand()
                self.hand_1_button.isActive = True #makes the button active once
            
        if self.hand_2_button.draw(self.game.display):
            if self.hand_2_button.isActive == False:
                self.game.player.add_Hand()
                self.hand_2_button.isActive = True    

        if self.hand_3_button.draw(self.game.display):
            if self.hand_3_button.isActive == False:
                self.game.player.add_Hand()
                self.hand_3_button.isActive = True    

        if self.hand_4_button.draw(self.game.display):
            if self.hand_4_button.isActive == False:
                self.game.player.add_Hand()
                self.hand_4_button.isActive = True    
            
        if self.hand_5_button.draw(self.game.display):
            if self.hand_5_button.isActive == False:
                self.game.player.add_Hand()
                self.hand_5_button.isActive = True    
            

        #TODO set up the hand placement
    
        #render the clickable button
        if self.back_button.draw(self.game.display):
            self.game.actions["back"] = True




    def update(self,actions):
        if actions["back"]:
            self.exit_state()
        self.game.reset_actions()