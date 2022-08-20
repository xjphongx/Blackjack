from Hand import Hand


class Player:
    def __init__(self):
        self.hand_list = Hand()

    def add_Hand(self):#Player can add a new hand when SPLITING
        hand = Hand()
        self.hand_list.append(hand)



    ####Player Actions: Hit, Stand, Split, Double
    def hit():
        pass
    def stand():
        pass
    def split():
        pass
    def double():
        pass