import pygame
from scripts.button import Button

class Bet_Menu():
    def __init__(self, game):
        self.game = game #get a reference to the game
        self.player_fund = game.player.fund
        self.x, self.y = self.game.display_width/2 , self.game.display_height - 50
        position_x_1, position_x_2, position_x_3 = self.x-270, self.x-180, self.x-90
        position_x_4 = self.x #center and fixed positions around the center
        position_x_5, position_x_6, position_x_7 = self.x+90, self.x+180, self.x+270
        IMAGE_SCALE = .25
        
        #intialize chip button objects
        white_chip_image = pygame.image.load("images/chips/white_chip_5.png").convert_alpha()
        red_chip_image = pygame.image.load("images/chips/red_chip_10.png").convert_alpha()
        blue_chip_image = pygame.image.load("images/chips/blue_chip_25.png").convert_alpha()
        green_chip_image = pygame.image.load("images/chips/green_chip_50.png").convert_alpha()
        black_chip_image = pygame.image.load("images/chips/black_chip_100.png").convert_alpha()
        yellow_chip_image = pygame.image.load("images/chips/yellow_chip_500.png").convert_alpha()
        allin_chip_image = pygame.image.load("images/chips/allin_chip.png").convert_alpha()
        self.white_chip_button = Button(position_x_1,self.y,white_chip_image,IMAGE_SCALE)
        self.red_chip_button = Button(position_x_2,self.y,red_chip_image,IMAGE_SCALE)
        self.blue_chip_button = Button(position_x_3,self.y,blue_chip_image,IMAGE_SCALE)
        self.green_chip_button = Button(position_x_4,self.y,green_chip_image,IMAGE_SCALE)
        self.black_chip_button = Button(position_x_5,self.y,black_chip_image,IMAGE_SCALE)
        self.yellow_chip_button = Button(position_x_6,self.y,yellow_chip_image,IMAGE_SCALE)
        self.allin_chip_button = Button(position_x_7, self.y,allin_chip_image,IMAGE_SCALE)

    #display all the buttons 
    def display(self):
        self.white_chip_button.draw(self.game.display)
        self.red_chip_button.draw(self.game.display)
        self.blue_chip_button.draw(self.game.display)
        self.green_chip_button.draw(self.game.display)
        self.black_chip_button.draw(self.game.display)
        self.yellow_chip_button.draw(self.game.display)
        self.allin_chip_button.draw(self.game.display)
        

