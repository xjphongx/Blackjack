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
        for i in range(8):     #shuffle the deck when starting the gameboard
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
        self.game.draw_text("How many hands are you playing?", 70, self.game.display_width/2,self.game.display_height/4)
        
        #TODO set up player input
        pygame.draw.rect(self.game.display, self.color, self.user_text_rect, 2)
        text_surface = self.input_font.render(self.user_text, True,(255,255,255))
        self.game.display.blit(text_surface, (self.user_text_rect.x+5,self.user_text_rect.y + 5)) #centers the text in the box
        
        self.user_text_rect.w = max(text_surface.get_width()+10, 100) #updates the textbox to dynamicly change size 

        #TODO set up the hand placement
    
        #render the clickable button
        if self.back_button.draw(self.game.display):
            self.game.actions["back"] = True




    def update(self,actions):
        if actions["back"]:
            self.exit_state()
        self.game.reset_actions()