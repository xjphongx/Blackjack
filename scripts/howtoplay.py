import pygame
from scripts.state import State
from scripts.button import Button

class HowToPlay(State):
    def __init__(self, game):
        super().__init__(game)
        self.back_x = 150
        self.back_y = 55
        back_image = pygame.image.load("images/buttons/back_button.png").convert_alpha()
        self.back_button = Button(self.back_x, self.back_y, back_image, .10)

    def render(self,display):
        display.fill(self.game.background_color)
        self.game.draw_text('How to Play', 100, self.game.display_width/2, self.game.display_height/10)
        #TODO - add text instructions 
        #TODO - add image instructions
        #TODO - think about adding multiple pages/states

        #render the clickable buttons
        if self.back_button.draw(self.game.display):
            self.game.actions["back"] = True
            

    def update(self,actions):
        #goes back to previous state by exiting current state
        if actions["back"]:
            self.exit_state()
        self.game.reset_actions()
