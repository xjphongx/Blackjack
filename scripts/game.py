import pygame,os
from scripts.state import BlackjackMenu, Gameboard, HowToPlayMenu
from scripts.turn_system import TurnSystem

class Game():
    def __init__(self):
        pygame.init()
        self.running = True 
        self.playing = False
        self.ESCAPE_KEY = False
        self.display_width = 1300
        self.display_height = 900
        self.display = pygame.Surface((self.display_width,self.display_height))
        self.screen = pygame.display.set_mode((self.display_width,self.display_height))
        self.screen_title = pygame.display.set_caption("Black Jack")
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.background_color = pygame.color.Color(0,132,113)
        self.font_path = os.path.abspath('font/BlackJack.ttf')
        self.blackjack_state = BlackjackMenu(self)
        self.howtoplay_state = HowToPlayMenu(self)#this is how to traverse different menus
        self.gameboard = Gameboard(self)
        self.current_state = self.blackjack_state #so i can change menus and states
        #self.turn_system = TurnSystem(self)
        
        
    
    #Function game_loop() contains all the game elements and objects
    def game_loop(self): 
        #game loop
        while self.playing:
            self.check_events()
            #TODO - add update function for players and dealer
            if isinstance(self.current_state, Gameboard):
                print("true")
                #if the current state is in the gameboard state
                #add player text input
              
                


            #TODO - add a play again or return to menu option
            #pygame.display.update()
            pygame.display.flip()
            self.clock.tick(self.FPS)
            self.reset_escape_key()
            break #used for testing 1 iteration

    #Function  check_events() checks for user input on pygame events     
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                self.current_state.run_display = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN: #event where player presses a key on the keyboard
                if event.key == pygame.K_ESCAPE:
                    self.ESCAPE_KEY = True

    def reset_escape_key(self):
        self.ESCAPE_KEY = False     

    def draw_text(self, text, text_size, x, y):
         font = pygame.font.Font(self.font_path, text_size)
         text_surface = font.render(text, True, (225,228,230))
         text_rect = text_surface.get_rect()
         text_rect.center = (x,y) #used to center the text
         self.display.blit(text_surface,text_rect)



