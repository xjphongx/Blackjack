import pygame, random, math
from scripts.button import Button
from scripts.player import Dealer, Player
from scripts.stack import DeckPile,DiscardPile
from scripts.turn_system import TurnSystem


IMAGE_SCALE = .15
#Abstract data class
class State():
    def __init__(self, game):
        self.game = game #reference to the game class
        self.center_width = self.game.display_width/2
        self.center_height = self.game.display_height/2
        self.run_display = True

    def blit_screen(self):
        self.game.screen.blit(self.game.display, (0,0))
        pygame.display.update()
        self.game.reset_escape_key()

#child class
class BlackjackMenu(State):
    def __init__(self, game):
        super().__init__(game)
        #play game button
        self.play_game_x = self.center_width
        self.play_game_y = self.center_height-100
        play_game_image = pygame.image.load("images/buttons/play_game_button.png").convert_alpha()
        self.play_game_button = Button(self.play_game_x,self.play_game_y, play_game_image, IMAGE_SCALE)
        #how to play button
        self.how_to_play_x = self.center_width
        self.how_to_play_y = self.center_height
        how_to_play_image = pygame.image.load("images/buttons/how_to_play_button.png").convert_alpha() 
        self.how_to_play_button = Button(self.how_to_play_x,self.how_to_play_y, how_to_play_image, IMAGE_SCALE)
        #quit button
        self.quit_x = self.center_width
        self.quit_y = self.center_height + 100
        quit_image = pygame.image.load("images/buttons/quit_button.png").convert_alpha()
        self.quit_button = Button(self.quit_x, self.quit_y, quit_image, IMAGE_SCALE)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.game.display.fill(self.game.background_color)
            #Draw the black jack title
            self.game.draw_text('Black Jack', 150, self.game.display_width/2, self.game.display_height/5)
            self.game.draw_text('Game by Jimmy Phong',20, 1200,885) #adding game credits to author
            #place menu stuff below
            self.check_input()
            self.blit_screen()

    def check_input(self):
        #draw all the buttons for functionality
        if self.play_game_button.draw(self.game.display):
            self.game.playing = True
            self.game.current_menu = self.game.gameboard
            #self.run_display = False

        elif self.how_to_play_button.draw(self.game.display):
            self.game.current_menu = self.game.howtoplay_menu

        elif self.quit_button.draw(self.game.display):
            self.game.playing = False
            self.game.running = False
        
        self.run_display = False

class HowToPlayMenu(State):
    def __init__(self, game):
        super().__init__(game)
        self.back_x = 150
        self.back_y = 55
        back_image = pygame.image.load("images/buttons/back_button.png").convert_alpha()
        self.back_button = Button(self.back_x, self.back_y, back_image, .10)
        #TODO - add text instructions 
        #TODO - add image instructions
        #TODO - think about adding multiple pages/states
    
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.game.display.fill(self.game.background_color)
            self.game.draw_text('How to Play', 100, self.game.display_width/2, self.game.display_height/10)
            #place menu stuff below
            self.check_input()
            self.blit_screen()

    def check_input(self):
        if self.back_button.draw(self.game.display):
            self.game.current_menu = self.game.blackjack_menu
            self.run_display = False #this stops the loop 10 lines above
            #^^^ this stops the CURRENT display

#this is the state where the game is being played
class Gameboard(State):
    def __init__(self, game):
        super().__init__(game)
        #initialize the game board objects
        self.dealer = Dealer()
        self.deck_pile = DeckPile()
        self.deck_pile.load_cards_to_deck()
        self.discard_pile = DiscardPile()
        for i in range(10):     #shuffle the deck when starting the gameboard
            self.deck_pile.cut_deck()
            self.deck_pile.casino_shuffle()
        #self.deck_pile.show()
        self.turn_system = TurnSystem(self.game)
        

        

    def display_menu(self):
        self.run_display = True
        print("gameboard display running")
        self.turn_system.intoduction()
        while self.run_display:
            self.game.check_events()
            self.game.display.fill(self.game.background_color)
            #set up dealer
            self.game.display.blit(self.dealer.dealer_image_surface, self.dealer.rect)           
            #set up deck
            self.game.display.blit(self.deck_pile.deck_back_image_surface, self.deck_pile.rect) 
            #set up discard pile
            self.game.display.blit(self.discard_pile.discard_pile_image_surface, self.discard_pile.rect)
            self.game.draw_text('Playing game', 100, self.game.display_width/2,self.game.display_height/10)            
            self.game.draw_text("How many hands are you playing?", 50, self.game.display_width/2,self.game.display_height/2)
            #get player hand amount input 
            


            self.check_input()
            self.blit_screen()


    def check_input(self):
        #add stuff here
        pass






