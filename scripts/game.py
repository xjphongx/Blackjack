import pygame,os, sys
from scripts.title import Title

class Game():
    def __init__(self):
        pygame.init()
        self.ESCAPE_KEY = False
        self.display_width, self.display_height = 1300, 900
        self.display = pygame.Surface((self.display_width,self.display_height))
        self.screen = pygame.display.set_mode((self.display_width,self.display_height))
        self.running = True
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.IMAGE_SCALE = 0.15
        self.screen_title = pygame.display.set_caption("Black Jack")
        self.background_color = pygame.color.Color(0,132,113)
        self.font_path = os.path.abspath('font/Milkalte.otf')
        self.state_stack = []
        self.load_states()
        self.actions = {
            "play":False,
            "howtoplay":False,
            "back":False,
            "next":False
        }
    
    def render(self):
        self.state_stack[-1].render(self.display)
        self.screen.blit(pygame.transform.scale(self.display,(self.display_width, self.display_height)),(0,0))
        pygame.display.flip()

    def update(self):
        self.state_stack[-1].update(self.actions) #add parameters?

    #Function game_loop() contains all the game elements and objects
    def game_loop(self): 
        print("gameloop") 
        #game loop
        while self.running:
            self.check_events()
            self.render()
            self.update()
            
            self.clock.tick(self.FPS)
            
    #Function  check_events() checks for user input on pygame events     
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("exiting")
                self.running = False
                self.playing = False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN: #event where player presses a key on the keyboard
                if event.key == pygame.K_ESCAPE:
                    self.ESCAPE_KEY = True

    def reset_actions(self):
        for key in self.actions:
            self.actions[key] = False                 

    def reset_escape_key(self):
        self.ESCAPE_KEY = False     

    def draw_text(self, text, text_size, x, y):
         #TODO Figure out how to prevent text from expanding both direction 
         font = pygame.font.Font(self.font_path, text_size)
         text_surface = font.render(text, True, (225,228,230))
         text_rect = text_surface.get_rect()
         text_rect.center = (x,y) #used to center the text
         self.display.blit(text_surface,text_rect)

    def load_states(self):
        #load the first state(Title) when game starts
        self.title_screen = Title(self) #this is similar to loading in constructor
        self.state_stack.append(self.title_screen) 

