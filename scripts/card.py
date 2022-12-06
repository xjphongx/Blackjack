import pygame

#Card Class
#@Parameters:
#@  type - Str value that represents the type of card
#@  pip_value - Int value that represents the numeric value of the card
#@  suit - Str value that represents what kind of suit: Spades, Clubs, Diamonds, and Hearts
#@  image - Str value that holds the path to the image directory
#
#Special cases include card_type "Ace" which will add two more class variables
#Ace cards are worth 1 or 11 depending on the current hand
#@  pip_value - sets the value to be 1
#@  high_pip_value - sets the value to be 11
#

class Card(pygame.sprite.Sprite):
    def __init__(self, type, pip_value, suit, image, card_back_image):
        super().__init__()
        self.type = type
        self.suit = suit
        if(type) == "Ace":
            self.pip_value=1         #used for Aces
            self.high_pip_value=11       #used for Aces
        else:
            self.pip_value = pip_value
        self.x, self.y = 1225,80
        self.card_back_surface = pygame.image.load(card_back_image).convert_alpha()
        self.card_back_surface = pygame.transform.rotozoom(self.card_back_surface,0,.2)
        self.isFaceDown = False
        self.image_surface = pygame.image.load(image).convert_alpha()
        self.image_surface = pygame.transform.rotozoom(self.image_surface,0,.2) #scales the image better
        self.rect = self.image_surface.get_rect(center = (self.x,self.y)) 
        self.delta_x, self.delta_y = 0 , 0 

    def reset(self)->None:
        self.x, self.y = 1225,80
        self.isFaceDown = False
        self.delta_x, self.delta_y = 0,0

        
        
   



