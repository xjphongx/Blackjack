
from scripts.ring import Ring

class Ring_Row():
    def __init__(self, game, gameboard):
        self.game = game
        self.gameboard = gameboard
        self.isEmpty = True

        #intialize ring objects
        self.ring_1 = Ring(self.game,self.gameboard,1150,645,order=1)
        self.ring_2 = Ring(self.game,self.gameboard,900,685,order=2)
        self.ring_3 = Ring(self.game,self.gameboard,650,700,order=3)
        self.ring_4 = Ring(self.game,self.gameboard,400,685,order=4)
        self.ring_5 = Ring(self.game,self.gameboard,150,645,order=5)

    #display function blits the ring images and updates if a chip is placed
    def display(self):
        self.ring_1.display()
        self.ring_2.display()
        self.ring_3.display()
        self.ring_4.display()
        self.ring_5.display()
        self.ring_1.update()
        self.ring_2.update()
        self.ring_3.update()
        self.ring_4.update()
        self.ring_5.update()

    #function clear sets all the ring's bools to false and clears player hand list
    def clear(self):
        print("clearing")
        self.ring_1.clear()
        self.ring_2.clear()
        self.ring_3.clear()
        self.ring_4.clear()
        self.ring_5.clear()
        self.isEmpty=True #ring row is empty
        self.game.player.clear_bets()
        

        