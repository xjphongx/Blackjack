
class Hand:
    def __init__(self): #add bet size when creating a hand, minimum bet
        self.card_in_hand_list = []
        self.bet_size = 0
        self.hand_sum = 0
        self.hand_size = 0

    #update hand after every removal of a card to prevent index error
    def update_hand(self):
        self.hand_size = len(self.card_in_hand_list)

    def get_size(self):
        return self.hand_size

    def reset_hand_sum(self):
        self.hand_sum = 0

    #when adding cards to my hand, add pip value as well
    def add_card_to_hand(self, card): 
        self.card_in_hand_list.append(card)
        self.hand_sum += card.pip_value
        self.hand_size+=1       #increase hand size when adding a card
    
    def remove_card_from_hand(self):
        #print(f"testing: {self.card_in_hand_list[-1]}")
        self.hand_sum -= self.card_in_hand_list[-1].pip_value
        return self.card_in_hand_list.pop()
         #Note: After every removal, call update_hand() to prevent index error

    
        
    