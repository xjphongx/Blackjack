import pygame
from scripts.button import Button

class Bet_Menu():
    def __init__(self, game):
        self.game = game #get a reference to the game
        #self.player_fund = game.player.fund
        #self.bet_amount = 0
        self.x, self.y = self.game.display_width/2 , self.game.display_height - 50
        self.bet_text_x, self.bet_text_y = self.x , self.y
        self.fund_text_x, self.fund_text_y = 1100,850
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
        clear_button_image = pygame.image.load("images/buttons/clear_button.png").convert_alpha()
        self.white_chip_button = Button(position_x_1,self.y,white_chip_image,IMAGE_SCALE)
        self.red_chip_button = Button(position_x_2,self.y,red_chip_image,IMAGE_SCALE)
        self.blue_chip_button = Button(position_x_3,self.y,blue_chip_image,IMAGE_SCALE)
        self.green_chip_button = Button(position_x_4,self.y,green_chip_image,IMAGE_SCALE)
        self.black_chip_button = Button(position_x_5,self.y,black_chip_image,IMAGE_SCALE)
        self.yellow_chip_button = Button(position_x_6,self.y,yellow_chip_image,IMAGE_SCALE)
        self.allin_chip_button = Button(position_x_7, self.y,allin_chip_image,IMAGE_SCALE)
        self.clear_button = Button(position_x_7,785,clear_button_image,scale=.04)

    #display all the buttons 
    def display(self):
        self.game.draw_text(f"Bet: {self.game.player.bet_amount}", 40, self.bet_text_x, self.bet_text_y-63)
        self.game.draw_text(f"Fund: {self.game.player.fund}", 40, self.fund_text_x, self.fund_text_y)
        if self.white_chip_button.draw(self.game.display):
            if 5 <= self.game.player.fund:
                self.game.player.fund -= 5
                self.game.player.bet_amount += 5
        if self.red_chip_button.draw(self.game.display):
            if 10 <= self.game.player.fund:
                self.game.player.fund -= 10
                self.game.player.bet_amount += 10
        if self.blue_chip_button.draw(self.game.display):
            if 25 <= self.game.player.fund:
                self.game.player.fund -= 25
                self.game.player.bet_amount += 25
        if self.green_chip_button.draw(self.game.display):
            if 50 <= self.game.player.fund:
                self.game.player.fund -= 50
                self.game.player.bet_amount += 50
        if self.black_chip_button.draw(self.game.display):
            if 100 <= self.game.player.fund:
                self.game.player.fund -= 100
                self.game.player.bet_amount += 100
        if self.yellow_chip_button.draw(self.game.display):
            if 500 <= self.game.player.fund:
                self.game.player.fund -= 500
                self.game.player.bet_amount += 500
        if self.allin_chip_button.draw(self.game.display):
            if self.game.player.fund != 0: #prevents 0 fund replacing bet amount
                self.game.player.bet_amount += self.game.player.fund
                self.game.player.fund = 0
        if self.clear_button.draw(self.game.display):
            self.game.player.fund += self.game.player.bet_amount
            self.game.player.bet_amount = 0
                
        #TODO add more functionality

