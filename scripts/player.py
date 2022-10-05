from bdb import effective
import pygame,os
from scripts.hand import Hand

DEALER_STARTING_FUND = 99999999999999999999999999999999999999999
PLAYER_STARTING_FUND = 1000
class Player():
    def __init__(self, fund = PLAYER_STARTING_FUND):
        self.hand_list = [5,4,3,2,1] 
        self.fund = fund
        self.is_player_turn = False
        self.action_list = {
            'hit':False, 
            'stand':False, 
            'split':False, 
            'double':False
            }

    def add_Hand(self, order):#Player can add a new hand when SPLITING
        hand = Hand(order) #create hand with a specific order
        new_index = self.hand_list.index(hand.order)
        self.hand_list.insert(new_index, hand) #add into list at the given index
        self.hand_list.remove(hand.order)      #remove the value from list
        print(f"{hand.order} : {hand}")
    def add_funds(self, added_amount):
        self.fund += added_amount
    def subtract_funds(self, subtracted_amount):
        self.fund -= subtracted_amount
    def move_hand_to_discard(self):
        pass

    ####Player Actions: Hit, Stand, Split, Double
    def hit():
        pass
    def stand():
        pass
    def split():
        pass
    def double():
        pass

class Dealer(Player,pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(fund = DEALER_STARTING_FUND)
        self.hand_list = [6]
        self.add_Hand(6)
        self.dealer_image_path = os.path.abspath('images/dealer.png')
        self.dealer_image_surface = pygame.image.load(self.dealer_image_path).convert_alpha()
        self.dealer_image_surface = pygame.transform.rotozoom(self.dealer_image_surface,0,.2)
        self.rect = self.dealer_image_surface.get_rect(midtop=(1300/2,20)) #screen dimension is 1300x900
