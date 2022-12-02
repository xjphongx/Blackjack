
import pygame,os
from scripts.hand import Hand

DEALER_STARTING_FUND = 99999999999999999999999999999999999999999
PLAYER_STARTING_FUND = 1000
class Player():
    def __init__(self, game, gameboard, fund = PLAYER_STARTING_FUND):
        self.game = game
        self.gameboard = gameboard
        self.hand_list = [1,2,3,4,5] 
        self.fund = fund
        self.win_amount = 0
        self.round_difference_amount=0
        self.current_bet = 0

    #function add_Hand takes a specified order and adds it to player hand list
    def add_Hand(self, order:int ,bet_amount:int, x:float , y:float, isDealer=None):#Player can add a new hand when SPLITING
        #edge case when it is the dealers hand
        if isDealer:
            hand = Hand(self.game, self.gameboard, order, x, y, bet_amount, isDealer)
        else:
            hand = Hand(self.game,self.gameboard, order, x, y,bet_amount) #create hand with a specific order
        
        new_index = self.hand_list.index(hand.order)
        self.hand_list.insert(new_index, hand) #add into list at the given index
        self.hand_list.remove(hand.order)      #remove the value from list
        print(f"{hand.order} : {hand}")

    #function split_hand will create a new hand and give it a card from the orignal hand
    def split_hand(self, hand:Hand, isExtra:bool ,bet_amount:int, x:float, y:float, isDealer:bool = False):
        #Create new Hand object 
        new_hand = Hand(game= self.game,
                    gameboard= self.gameboard,
                    order= hand.order,
                    x= x-60,
                    y = y,
                    bet_amount=bet_amount,
                    isDealer= isDealer,
                    isExtra= isExtra)
        #set the newhand to have a chip
        new_hand.hasChip=True
        hand.hasChip = True
        if hand.order in self.gameboard.ring_row.ring_map.keys():
            #get the ring's chip
            new_hand.chip = self.gameboard.ring_row.ring_map[hand.order].chip 
            #get the ring's x and y coordinates
            new_hand.chip_x = new_hand.x - 30
            new_hand.chip_y = new_hand.y + 150
            #same thing but for the original chip
            hand.chip = self.gameboard.ring_row.ring_map[hand.order].chip 
            hand.chip_x = hand.x + 30
            hand.chip_y = hand.y + 150
            #remove the ring's chip for visual affects
            self.gameboard.ring_row.ring_map[hand.order].chip = self.gameboard.ring_row.ring_map[hand.order].empty_button.image

        #Places the new hand into the correct index in the turn list
        new_hand.add_card(hand.remove_card())
        new_hand.placement.y = hand.card_list[-1].rect.y
        new_hand.card_list[-1].rect.x = new_hand.placement.x - 45
        new_hand.card_list[-1].rect.y = new_hand.placement.y
        #Hard code to readjust the new hand's next cards's placement
        new_hand.placement.x = hand.x-90
        new_hand.placement.y = hand.y-20
        #insert into turn list
        new_index = self.gameboard.turn_list.index(hand)+1  #the NEXT index
        self.gameboard.turn_list.insert(new_index,new_hand) #inserts into the correct index

    def remove_Hand(self,order):
        pass
    
    def add_funds(self, added_amount):
        self.fund += added_amount
    def subtract_funds(self, subtracted_amount):
        self.fund -= subtracted_amount

    def clear_bets(self):
        self.hand_list.clear() #list function to clear list
        self.hand_list = [1,2,3,4,5] #sets the hand list to default order

    def reset_UI(self):
        self.current_bet = 0
        self.win_amount = 0
        self.round_difference_amount = 0    
    
    def move_hand_to_discard(self):
        pass


class Dealer(Player,pygame.sprite.Sprite):
    def __init__(self, game, gameboard):
        super().__init__(game, gameboard, fund = DEALER_STARTING_FUND)
        self.hand_list = [6] #puts the dealer last in the turn list
        self.add_Hand(order= 6,x= 750,y= 225, bet_amount=0,isDealer = True)
        self.dealer_image_path = os.path.abspath('images/dealer.png')
        self.dealer_image_surface = pygame.image.load(self.dealer_image_path).convert_alpha()
        self.dealer_image_surface = pygame.transform.rotozoom(self.dealer_image_surface,0,.2)
        self.rect = self.dealer_image_surface.get_rect(midtop=(1300/2,20)) #screen dimension is 1300x900
