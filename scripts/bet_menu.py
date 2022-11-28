import pygame
from scripts.button import Button

class Bet_Menu():
    def __init__(self, game, gameboard):
        self.game = game #get a reference to the game
        self.gameboard = gameboard #to get a reference to the gameboard
        self.x, self.y = self.game.display_width/2 , self.game.display_height - 50
        self.bet_text_x, self.bet_text_y = self.x , self.y
        self.fund_text_x, self.fund_text_y = 1100,850
        position_x_1, position_x_2, position_x_3 = self.x-270, self.x-180, self.x-90
        position_x_4 = self.x #center and fixed positions around the center
        position_x_5, position_x_6, position_x_7 = self.x+90, self.x+180, self.x+270
        IMAGE_SCALE = .25
        self.min_bet = self.gameboard.min_bet #may change 
        
        #intialize chip button objects
        self.white_chip_image = pygame.image.load("images/chips/white_chip_5.png").convert_alpha()
        self.red_chip_image = pygame.image.load("images/chips/red_chip_10.png").convert_alpha()
        self.blue_chip_image = pygame.image.load("images/chips/blue_chip_25.png").convert_alpha()
        self.green_chip_image = pygame.image.load("images/chips/green_chip_50.png").convert_alpha()
        self.black_chip_image = pygame.image.load("images/chips/black_chip_100.png").convert_alpha()
        self.yellow_chip_image = pygame.image.load("images/chips/yellow_chip_500.png").convert_alpha()
        self.allin_chip_image = pygame.image.load("images/chips/allin_chip.png").convert_alpha()
        clear_button_image = pygame.image.load("images/buttons/clear_button.png").convert_alpha()
        self.white_chip_button = Button(position_x_1,self.y,self.white_chip_image,IMAGE_SCALE)
        self.red_chip_button = Button(position_x_2,self.y,self.red_chip_image,IMAGE_SCALE)
        self.blue_chip_button = Button(position_x_3,self.y,self.blue_chip_image,IMAGE_SCALE)
        self.green_chip_button = Button(position_x_4,self.y,self.green_chip_image,IMAGE_SCALE)
        self.black_chip_button = Button(position_x_5,self.y,self.black_chip_image,IMAGE_SCALE)
        self.yellow_chip_button = Button(position_x_6,self.y,self.yellow_chip_image,IMAGE_SCALE)
        self.allin_chip_button = Button(position_x_7, self.y,self.allin_chip_image,IMAGE_SCALE)
        self.clear_button = Button(position_x_7,785,clear_button_image,scale=.04)
        

    #display all the buttons 
    def display(self):
        self.game.draw_text(f"Min Bet: {self.min_bet}", 40,self.bet_text_x-250, self.bet_text_y-63)
        self.game.draw_text(f"Current Bet: {self.gameboard.player.current_bet}", 40, self.bet_text_x, self.bet_text_y-63)
        self.game.draw_text(f"Round Won: {self.gameboard.player.win_amount}",30, self.fund_text_x, self.fund_text_y-70)
        self.game.draw_text(f"Round Difference: {self.gameboard.player.round_difference_amount}", 30, self.fund_text_x,self.fund_text_y-35)
        self.game.draw_text(f"Fund: {self.gameboard.player.fund}", 40, self.fund_text_x, self.fund_text_y)
        #if statements will work if button is clicked and the game is not active
        if self.white_chip_button.draw(self.game.display) and not self.gameboard.confirm_button.isActive:
            if 5 <= self.gameboard.player.fund:
                self.gameboard.player.fund -= 5
                self.gameboard.player.current_bet += 5
                self.gameboard.cursor.chip = self.white_chip_button.image

        if self.red_chip_button.draw(self.game.display) and not self.gameboard.confirm_button.isActive:
            if 10 <= self.gameboard.player.fund:
                self.gameboard.player.fund -= 10
                self.gameboard.player.current_bet += 10
                self.gameboard.cursor.chip = self.red_chip_button.image

        if self.blue_chip_button.draw(self.game.display) and not self.gameboard.confirm_button.isActive:
            if 25 <= self.gameboard.player.fund:
                self.gameboard.player.fund -= 25
                self.gameboard.player.current_bet += 25
                self.gameboard.cursor.chip = self.blue_chip_button.image

        if self.green_chip_button.draw(self.game.display) and not self.gameboard.confirm_button.isActive:
            if 50 <= self.gameboard.player.fund:
                self.gameboard.player.fund -= 50
                self.gameboard.player.current_bet += 50
                self.gameboard.cursor.chip = self.green_chip_button.image

        if self.black_chip_button.draw(self.game.display) and not self.gameboard.confirm_button.isActive:
            if 100 <= self.gameboard.player.fund:
                self.gameboard.player.fund -= 100
                self.gameboard.player.current_bet += 100
                self.gameboard.cursor.chip = self.black_chip_button.image

        if self.yellow_chip_button.draw(self.game.display) and not self.gameboard.confirm_button.isActive:
            if 500 <= self.gameboard.player.fund:
                self.gameboard.player.fund -= 500
                self.gameboard.player.current_bet += 500
                self.gameboard.cursor.chip = self.yellow_chip_button.image

        if self.allin_chip_button.draw(self.game.display) and not self.gameboard.confirm_button.isActive:
            if self.gameboard.player.fund != 0: #prevents 0 fund replacing bet amount
                self.gameboard.player.current_bet += self.gameboard.player.fund
                self.gameboard.player.fund = 0
                self.gameboard.cursor.chip = self.allin_chip_button.image

        #clears the whole ring row if the game is not active
        if self.clear_button.draw(self.game.display) and not self.gameboard.confirm_button.isActive:
            self.gameboard.player.fund += self.gameboard.player.current_bet
            self.gameboard.player.current_bet = 0
            self.gameboard.cursor.chip = None #resets cursor chip when pressed clear
            self.gameboard.ring_row.clear()
        #clears the chip in cursor and current bet, if the game is active
        elif self.gameboard.confirm_button.isActive:
            #self.gameboard.player.round_difference_amount = 0
            self.gameboard.cursor.chip = None

        #TODO add more functionality
        self.gameboard.cursor.update() #updates the cursor with the last chip image





