import pygame
from scripts.button import Button

IMAGE_SCALE = .15

class Menu():
    def __init__(self, game):
        self.game = game #reference to the game class
        self.center_width = self.game.display_width/2
        self.center_height =self.game.display_height/2
        self.run_display = True

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0,0))
        pygame.display.update()
        self.game.reset_escape_key()

class BlackjackMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.state = "BlackjackMenu" #starting up menu 
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
            #place menu stuff below
            self.check_input()
            self.blit_screen()


    def check_input(self):
        #Draw the black jack title
        self.game.draw_text('Black Jack', 150, self.game.display_width/2, self.game.display_height/5)
        self.game.draw_text('Game by Jimmy Phong',20, 1200,885) #adding game credits to author
        #draw all the buttons for functionality
        if self.play_game_button.draw(self.game.display):
            self.state = 'PlayGame'
            self.game.playing = True
        elif self.how_to_play_button.draw(self.game.display):
            self.state = 'HowToPlayMenu'
        elif self.quit_button.draw(self.game.display):
            self.state = 'Quit'
            self.game.playing = False
            self.game.running = False
        
        self.run_display = False

class HowToPlayMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.state = "HowToPlayMenu"
        #add back button
        self.back_x = self.center_width
        self.back_y = self.center_height
        back_image = pygame.image.load("images/buttons/back_button.png").convert_alpha()
        self.back_button = Button(self.back_x, self.back_y, back_image, IMAGE_SCALE)
        #add text instructions 
        #add image instructions
        #think about adding multiple pages/states
    
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.game.display.fill(self.game.background_color)
            self.check_input()
            self.blit_screen()

    def check_input(self):
        if self.back_button.draw(self.game.display):
            self.game.current_menu = self.game.blackjack_menu