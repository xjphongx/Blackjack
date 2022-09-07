import pygame
import os


#import sys
#from button import Button


class Game():
    def __init__(self):
        pygame.init()
        self.running = True 
        self.playing = False
        self.ESCAPE_KEY = False
        self.display_width = 1300
        self.display_height = 900
        self.display = pygame.Surface((self.display_width,self.display_height))
        self.window = pygame.display.set_mode((self.display_width,self.display_height))
        self.window_title = pygame.display.set_caption("Black Jack")
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.font_path = os.path.abspath('font/BlackJack.ttf')
        #self.font = pygame.font.SysFont("arial",140)
        #self.font = pygame.font.Font('blackjack.otf',)
        
        

    def game_loop(self):
        while self.playing:
            self.check_events()
            self.display.fill((0,132,113))
            self.draw_text('Thanks for Playing', 110, self.display_width/2, self.display_height/2)
            self.window.blit(self.display,(0,0))
            #add a play again or return to menu option
            pygame.display.update()
            self.clock.tick(self.FPS)
            self.reset_escape_key()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
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



