


class Hand:
    def __init__(self):
        self.card_in_hand_list = []
        self.hand_sum = 0
        self.hand_size = 0

    def update_hand(self):
        self.hand_size = len(self.card_in_hand_list)

    def get_size(self):
        return self.hand_size

    #when adding cards to my hand, add pip value as well
    def add_card_to_hand(self, card): 
        self.card_in_hand_list.append(card)
        self.hand_size+=1       #increase hand size when adding a card
    
    def add_cardpip_to_sum(self,card_pip_value):
        self.hand_sum += card_pip_value

    def remove_card_from_hand(self):
        return self.card_in_hand_list.pop()
        #Note: After every removal, call update_hand() to prevent index error

    def subtrack_cardpip_from_sum(self, card_pip_value):
        self.hand_sum -= card_pip_value