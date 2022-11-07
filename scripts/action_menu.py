import pygame
from scripts.button import Button

class Action_Menu():
    def __init__(self, hand, game, gameboard, x, y):
        self.hand = hand
        self.game = game
        self.gameboard = gameboard
        self.x = x + 75 #offset away from the hand center
        self.y = y - 100
        SCALE = .07
        OFFSET = 35
        #intialize button objects
        self.hit_button_image = pygame.image.load("images/buttons/wood_button_hit.png").convert_alpha()
        self.double_button_image = pygame.image.load("images/buttons/wood_button_double.png").convert_alpha()
        self.split_button_image = pygame.image.load("images/buttons/wood_button_split.png").convert_alpha()
        self.stand_button_image = pygame.image.load("images/buttons/wood_button_stand.png").convert_alpha()
        self.hit_button = Button(self.x, self.y, self.hit_button_image, scale=SCALE)
        self.double_button = Button(self.x, self.y+OFFSET, self.double_button_image, scale=SCALE)
        self.split_button = Button(self.x, self.y+(OFFSET*2), self.split_button_image, scale=SCALE)
        self.stand_button = Button(self.x, self.y+(OFFSET*3), self.stand_button_image, scale=SCALE)

    def display(self):
        if self.hit_button.draw(self.game.display):
            self.gameboard.hit(self.hand)
        
        self.double_button.draw(self.game.display)
        self.split_button.draw(self.game.display)
        if self.stand_button.draw(self.game.display):
            self.hand.stand = True
            self.hand.isTurn = False
            