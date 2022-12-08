import pygame
from scripts.state import State
from scripts.button import Button

class Tutorial(State):
    def __init__(self, game):
        super().__init__(game)
        self.back_x = 150
        self.back_y = 55
        column_offset = game.display_width/6
        self.column_x = column_offset
        self.column_x_2= column_offset*3
        self.column_x_3= self.column_x*5 
        self.image_row_y = 600
        back_image = pygame.image.load("images/buttons/back_button.png").convert_alpha()
        self.back_button = Button(self.back_x, self.back_y, back_image, .10)
        next_image = pygame.image.load("images/buttons/next_button.png").convert_alpha()
        self.next_button = Button(game.display_width-self.back_x, self.back_y, next_image, .10)
        self.image_1 = pygame.image.load("images/tutorial_image1.png").convert_alpha()
        self.image_1 = pygame.transform.rotozoom(self.image_1,0,.98)
        self.image_1_rect = self.image_1.get_rect(center=(self.column_x,self.image_row_y))
        
        self.image_2 = pygame.image.load("images/tutorial_image2.png").convert_alpha()
        self.image_2 = pygame.transform.rotozoom(self.image_2,0,.98)
        self.image_2_rect = self.image_2.get_rect(center=(self.column_x_2,self.image_row_y))

        self.image_3 = pygame.image.load("images/tutorial_image3.png").convert_alpha()
        self.image_3 = pygame.transform.rotozoom(self.image_3,0,.98)
        self.image_3_rect = self.image_3.get_rect(center=(self.column_x_3,self.image_row_y))


    def render(self,display):
        display.fill(self.game.background_color)
        self.game.draw_text('How to Play', 100, self.game.display_width/2, self.game.display_height/10)
        #TODO - add text instructions 
        self.game.draw_text('Objective: ', 70, self.back_x+50, self.back_y +125)
        self.game.draw_text('Beat the Dealer by... ', 50, self.back_x+125, self.back_y +200)
        self.game.draw_text("1) drawing a hand value higher", 25, self.column_x, self.back_y +250)
        self.game.draw_text("than dealer's hand value",25, self.column_x,self.back_y+290)
        self.game.display.blit(self.image_1,self.image_1_rect)

        self.game.draw_text("2) having the dealer's hand", 25, self.column_x_2, self.back_y +250)
        self.game.draw_text("value over 21",25, self.column_x_2,self.back_y+290)
        self.game.display.blit(self.image_2,self.image_2_rect)

        self.game.draw_text("3) drawing a hand value of", 25, self.column_x_3, self.back_y +250)
        self.game.draw_text("21 on the first two cards",25, self.column_x_3,self.back_y+290)
        self.game.display.blit(self.image_3,self.image_3_rect)

        #TODO - add image instructions
        #TODO - think about adding multiple pages/states
        #render the clickable buttons
        if self.back_button.draw(self.game.display):
            self.game.actions["back"] = True
        elif self.next_button.draw(self.game.display):
            self.game.actions["next"] = True
            
    def update(self,actions):
        #goes back to previous state by exiting current state
        if actions["back"]:
            self.exit_state()
        elif actions["next"]:
            next_state = Tutorial_2(self.game)
            next_state.enter_state()
        self.game.reset_actions()

class Tutorial_2(State):
    def __init__(self, game):
        super().__init__(game)
        self.back_x = 150
        self.back_y = 55
        back_image = pygame.image.load("images/buttons/back_button.png").convert_alpha()
        self.back_button = Button(self.back_x, self.back_y, back_image, .10)
        next_image = pygame.image.load("images/buttons/next_button.png").convert_alpha()
        self.next_button = Button(game.display_width-self.back_x, self.back_y, next_image, .10)
        self.tutorial_image = pygame.image.load("images/tutorial_image.png").convert_alpha()
        self.tutorial_image = pygame.transform.rotozoom(self.tutorial_image,0,.76)
        self.tutorial_image_rect = self.tutorial_image.get_rect(center=(game.display_width/2, (game.display_height/2)+75))

    def render(self,display):
        self.prev_state.render(display)
        display.fill(self.game.background_color)
        self.game.draw_text('How to Play', 100, self.game.display_width/2, self.game.display_height/10)
        self.game.display.blit(self.tutorial_image,self.tutorial_image_rect)
        if self.back_button.draw(self.game.display):
            self.game.actions["back"] = True
        elif self.next_button.draw(self.game.display):
            self.game.actions["next"] = True
    
    def update(self,actions):
        if actions["back"]:
            self.exit_state()
        elif actions["next"]:
            next_state = Tutorial_3(self.game)
            next_state.enter_state() #go to the previous state(tutorial 1)
        self.game.reset_actions()

class Tutorial_3(State):
    def __init__(self, game):
        super().__init__(game)
        self.back_x = 150
        self.back_y = 55
        back_image = pygame.image.load("images/buttons/back_button.png").convert_alpha()
        self.back_button = Button(self.back_x, self.back_y, back_image, .10)

    def render(self,display):
        self.prev_state.render(display)
        display.fill(self.game.background_color)
        self.game.draw_text('How to Play', 100, self.game.display_width/2, self.game.display_height/10)
        if self.back_button.draw(self.game.display):
            self.game.actions["back"] = True
    
    def update(self,actions):
        if actions["back"]:
            self.exit_state()
        self.game.reset_actions()



