import pygame
from scripts.button import Button



class Action_Menu():
    def __init__(self, hand, game, gameboard, x, y):
        self.hand = hand
        self.game = game
        self.gameboard = gameboard
        self.isInit = False
        self.x, self.y = x + 75, y - 100 #offset away from the hand center
        self.original_x, self.original_y = x+75, y-100 
        SCALE = .07
        #intialize button objects
        self.hit_button_image = pygame.image.load("images/buttons/wood_button_hit.png").convert_alpha()
        self.double_button_image = pygame.image.load("images/buttons/wood_button_double.png").convert_alpha()
        self.split_button_image = pygame.image.load("images/buttons/wood_button_split.png").convert_alpha()
        self.stand_button_image = pygame.image.load("images/buttons/wood_button_stand.png").convert_alpha()
        self.hit_button = Button(self.x, self.y, self.hit_button_image, scale=SCALE)
        self.double_button = Button(self.x, self.y, self.double_button_image, scale=SCALE)
        self.split_button = Button(self.x, self.y, self.split_button_image, scale=SCALE)
        self.stand_button = Button(self.x, self.y, self.stand_button_image, scale=SCALE)

    def reset_placement(self):
        self.x = self.original_x
        self.y = self.original_y
        self.isInit = False
    
    #This section of code allows Dynamic relocation of the player's possible playing options
    def init_dynamic_buttons(self):
        if self.isInit == False:
            
            if self.hand.hand_sum == 21:
                self.y -=35 #move the original placement down
            self.hit_button.rect.center = (self.x, self.y)

            self.y += 35 #places the next y coordinate
            #if hand can double down, update the button's next y coordinate
            if len(self.hand.card_list) <= 2 and self.hand.hand_sum <=11 and self.gameboard.player.fund > self.hand.bet_amount:
                self.double_button.rect.center = (self.x, self.y) #the next coor
                self.y += 35 #updates next y coordinate
            #if hand can split, update the button's next y coordinate
            if self.hand.card_list[0].type == self.hand.card_list[1].type and len(self.hand.card_list) == 2:
                self.split_button.rect.center = (self.x,self.y)
                self.y += 35 #updates next y coordinate
            #Update Stand's coordinates
            self.stand_button.rect.center = (self.x, self.y)
            self.y += 35
            self.isInit = True #run once

#TODO make the menu dynamicly relocate base on avaiable player options
    def display(self):
        #Allows Dynamic buttons to appear
        self.init_dynamic_buttons()
        
        #HIT HAND BUTTON
        if self.hand.hand_sum != 21:
            if self.hit_button.draw(self.game.display):
                self.gameboard.hit(self.hand)
                self.reset_placement() #resets for next available options
     
        #DOUBLE DOWN BUTTON
        #check if hand is doubleable, if the first 2 cards are less than 11
        if len(self.hand.card_list) <= 2 and self.hand.hand_sum <=11 and self.gameboard.player.fund > self.hand.bet_amount:
            if self.double_button.draw(self.game.display):
                #player hits 1 cards side ways (pygame image rotation)
                self.gameboard.deck_pile.top().image_surface= pygame.transform.rotate(surface=self.gameboard.deck_pile.top().image_surface, angle = 90)
                self.gameboard.hit(self.hand)
                #add more funds equal to current bet from player funds and subtract from player's fund
                self.gameboard.player.fund -= self.hand.bet_amount #subtract funds
                self.gameboard.player.current_bet += self.hand.bet_amount #update current round bet
                self.hand.bet_amount = self.hand.bet_amount*2 #update hand bet amount
                self.hand.stand = True#ends the hand's turn
        #SPLIT BUTTON 
        #Check if hands has matching pairs 
        if self.hand.card_list[0].type == self.hand.card_list[-1].type:
            if self.split_button.draw(self.game.display):       
                #subtract funds and update UI
                self.gameboard.player.fund -= self.hand.bet_amount
                self.gameboard.player.current_bet += self.hand.bet_amount
                #create a new test hand next
                self.gameboard.player.split_hand(hand=self.hand,
                                               isExtra=True,
                                                bet_amount=self.hand.bet_amount,
                                                x=self.hand.x,
                                                y=self.hand.y,
                                                isDealer=False)
                #Moves the hand to the right
                self.hand.x += 60
                #reverts to the last known placement
                self.hand.placement.x = self.hand.x-20
                self.hand.placement.y = self.hand.y-20
                #shifts the card to the right
                for i , card in enumerate(self.hand.card_list):
                    card.rect.x += 60
                #Pass out new cards to both hands and continue to play
                current_index = self.gameboard.turn_list.index(self.hand)
                self.gameboard.hit(self.hand)
                self.gameboard.hit(self.gameboard.turn_list[current_index+1])    
                #shifts the action menu buttons 
                #self.hit_button.update_coordinates(x=self.hit_button.rect.x+100,y=self.hit_button.rect.y)
                #self.double_button.update_coordinates(x=self.double_button.rect.x+100,y=self.double_button.rect.y)
                #self.split_button.update_coordinates(x=self.split_button.rect.x+100,y=self.split_button.rect.y)
                #self.stand_button.update_coordinates(x=self.stand_button.rect.x+100,y=self.stand_button.rect.y)
                self.original_x += 60
                self.reset_placement() #resets for next available options
                print(f"handsum: {self.hand.hand_sum}")
                print(f"handuppersum: {self.hand.hand_upper_sum}")
                
        
        #STAND BUTTON        
        if self.stand_button.draw(self.game.display):
            self.hand.stand = True
            
