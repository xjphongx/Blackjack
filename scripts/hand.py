from scripts.placement import Placement

class Hand():
    def __init__(self, game, order,x ,y, isDealer = False): #add bet size when creating a hand, minimum bet
        self.game = game #reference to the game
        self.order = order #the hand's order
        self.x, self.y = x, y
        self.placement = Placement(x,y)
        self.isDealer = isDealer
        self.card_list = []
        self.min_bet = 50
        self.hasAce = False
        self.hand_sum = 0
        self.hand_upper_sum = 0 #calculated for ace edge case
        self.hand_size = 0
        self.player_action_menu = [] #LOOK AT TUTORIAL
        self.isTurn = False
        #need to add a small menu containing buttons for player to press 

    #function display updates the pygame game display with cards
    def display(self, display):
        for i, card in enumerate(self.card_list):
            #if card is faced down
            if card.isFaceDown:
                display.blit(card.card_back_surface, card.rect)
            else:
                display.blit(card.image_surface, card.rect)

        #only show the player's hand sum
        if not self.isDealer:
            #display the hand sums 
            if self.hasAce:
                self.game.draw_text(f"{self.hand_sum} or {self.hand_upper_sum}",30,self.x, self.y+90)   
            else:
                self.game.draw_text(f"{self.hand_sum}",30,self.x, self.y+90)
            
        

    #print out on terminal the contains of the card_list
    def show(self):
        for i, card in enumerate(self.card_list) :
            print(card.type, end= " ")  
        print()  
    
    #reset hand total sum to zero
    def reset_hand_sum(self):
        self.hand_sum = 0

    #when adding cards to my hand, add pip value as well
    def add_card(self, card): 
        #set hand_sum to be the lower sum and hand uppper is uppper sum
        if card.type == 'Ace':
            self.hasAce = True
            self.hand_sum += card.low_pip_value
            self.hand_upper_sum += card.high_pip_value
        else:
            self.hand_sum += card.pip_value
            self.hand_upper_sum += card.pip_value
        self.card_list.append(card) 
        self.hand_size+=1       #increase hand size when adding a card
        
    def remove_card(self):
        self.hand_sum -= self.card_list[-1].pip_value
        temp_card = self.card_list.pop()
        self.hand_size = len(self.card_list) #update hand size after pop, to prevent error
        return temp_card
         




        
    
