import pygame
from scripts.state import State
from scripts.button import Button

class Title(State):
    def __init__(self, game):
        super().__init__(game)
        IMAGE_SCALE = 0.15
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

    def update(self):
        pass
    
    def render(self, display):
        #render all title screen objects here
        display.fill(self.game.background_color)
        display.fill(self.game.background_color)
        self.game.draw_text('Black Jack', 150, self.game.display_width/2, self.game.display_height/5)
        self.game.draw_text('Game by Jimmy Phong',20, 1200,885) #adding game credits to author    

        #render the clickable buttons 
        if self.play_game_button.draw(self.game.display):
            print("clicked play")
            self.game.current_state = self.game.gameboard_state           
            #self.game.playing = True
            #self.run_display = False
        elif self.how_to_play_button.draw(self.game.display):
            self.game.current_state = self.game.howtoplay_state
            #self.run_display = False
        elif self.quit_button.draw(self.game.display):
            print("quit")
            pygame.quit()
            exit()
            #self.game.playing = False
            #self.game.running = False
            #self.run_display = False
    