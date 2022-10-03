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
        self.prev_state = None
        self.center_width = self.game.display_width/2
        self.center_height = self.game.display_height/2
        self.run_display = True

    def update(self):
        pass
    def render(self, surface):
        pass

    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self) #add the object into stack

    def exit_state(self):
        self.game.state_stack.pop()

    def blit_screen(self):
        self.game.screen.blit(self.game.display, (0,0))
        pygame.display.update()
        

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

    def display(self):
        print("blackjack state")
        self.run_display = True 
        while self.run_display:
            print("running while loopp")
            self.game.check_events()
            #Draw the black jack title
            self.game.display.fill(self.game.background_color)
            self.game.draw_text('Black Jack', 150, self.game.display_width/2, self.game.display_height/5)
            self.game.draw_text('Game by Jimmy Phong',20, 1200,885) #adding game credits to author
            #place menu stuff below    
            self.check_input()

            #print(f"checking boolean {self.run_display}")
            self.blit_screen()
            #print(f"checking boolean {self.run_display}")

        #if self.run_display == False:
            #print("breaking")
                

    def check_input(self):
        #draw all the buttons for functionality
        if self.play_game_button.draw(self.game.display):
            print("clicked play")
            self.game.current_state = self.game.gameboard_state           
            self.game.playing = True
            self.run_display = False
        elif self.how_to_play_button.draw(self.game.display):
            self.game.current_state = self.game.howtoplay_state
            self.run_display = False
        elif self.quit_button.draw(self.game.display):
            print("quit")
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
    
    def display(self):
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
            self.game.current_state = self.game.blackjack_state
            self.run_display = False #this stops the loop 10 lines above
            #^^^ this stops the CURRENT display

#this is the state where the game is being played
class Gameboarde(State):
    def __init__(self, game):
        super().__init__(game)
        #initialize the game board objects
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


    def display(self):
        print("display gameboard")
        self.run_display = True   
        while self.run_display:
            self.game.check_events()
            self.game.display.fill(self.game.background_color)
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

            self.check_input()
            self.blit_screen()

    def check_input(self):
        #add stuff here
        if self.back_button.draw(self.game.display):
            self.game.current_state = self.game.blackjack_state
            self.run_display = False
            self.game.playing = False






