import pygame,os
from scripts.state import BlackjackMenu, Gameboard, HowToPlayMenu
from scripts.title import Title
from scripts.turn_system import TurnSystem

class Game():
    def __init__(self):
        pygame.init()
        self.ESCAPE_KEY = False
        self.display_width = 1300
        self.display_height = 900
        self.display = pygame.Surface((self.display_width,self.display_height))
        self.screen = pygame.display.set_mode((self.display_width,self.display_height))
        self.running = True 
        self.playing = True
        self.screen_title = pygame.display.set_caption("Black Jack")
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.background_color = pygame.color.Color(0,132,113)
        self.font_path = os.path.abspath('font/BlackJack.ttf')
        self.state_stack = []
        self.load_states()

        self.blackjack_state = BlackjackMenu(self)
        self.howtoplay_state = HowToPlayMenu(self)#this is how to traverse different menus
        self.gameboard_state = Gameboard(self)
        self.current_state = self.blackjack_state #so i can change menus and states
        #self.turn_system = TurnSystem(self)
        #self.base_font = pygame.font.Font(None,32)
        #self.user_text = 'test' #recieve player input 
        
    def update(self):
        self.state_stack[-1].update() #add parameters?

    def render(self):
        self.state_stack[-1].render(self.display)
        self.screen.blit(pygame.transform.scale(self.display,(self.display_width, self.display_height)),(0,0))
        pygame.display.flip()


    #Function game_loop() contains all the game elements and objects
    def game_loop(self): 
        print("gameloop")
        
        #game loop
        while self.playing:
            print("while looop in gameloop")
            self.check_events()
            #TODO - add update function for players and dealer
            if isinstance(self.current_state, Gameboard):
                print("entering gameboard state")
                
            #TODO - add a play again or return to menu option
        
            self.update()
            self.render()
            #self.clock.tick(self.FPS)
            #self.reset_escape_key()
            #used for testing 1 iteration
            #break #TODO I have to pause this loop for player to hit hand and etc
            

    #Function  check_events() checks for user input on pygame events     
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("exiting")
                self.running = False
                self.playing = False
                #self.current_state.run_display = False
                pygame.quit()
                exit()
            
            if event.type == pygame.KEYDOWN: #event where player presses a key on the keyboard
                if event.key == pygame.K_ESCAPE:
                    self.ESCAPE_KEY = True
                #self.user_text += event.unicode
                if event.key == pygame.K_BACKSPACE:
                    self.gameboard_state.user_text = self.gameboard_state.user_text[0:-1]
                else:
                    self.gameboard_state.user_text += event.unicode
                if event.key == pygame.K_RETURN:
                    #TODO Take user input of ONLY 1-5 hands, try and except
                    # case: if NOT 1-5, EMPTY user_text, draw_text invalid input try again
                    print("enter")
                    

    def reset_escape_key(self):
        self.ESCAPE_KEY = False     

    def draw_text(self, text, text_size, x, y):
         font = pygame.font.Font(self.font_path, text_size)
         text_surface = font.render(text, True, (225,228,230))
         text_rect = text_surface.get_rect()
         text_rect.center = (x,y) #used to center the text
         self.display.blit(text_surface,text_rect)

    def load_states(self):
        self.title_screen = Title(self) #this is similar to loading in constructor
        self.state_stack.append(self.title_screen)

