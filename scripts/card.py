import pygame


#Card Class
#@Parameters:
#@  card_type - Str value that represents the type of card
#@  pip_value - Int value that represents the numeric value of the card
#@  suit - Str value that represents what kind of suit: Spades, Clubs, Diamonds, and Hearts
#
#Special cases include card_type "Ace" which will add two more class variables
#Ace cards are worth 1 or 11 depending on the current hand
#@  low_pip_value - sets the value to be 1
#@  high_pip_value - sets the value to be 11
#

class Card(pygame.sprite.Sprite):
    def __init__(self, card_type, pip_value, suit, card_image):
        super().__init__()
        self.card_type = card_type
        self.pip_value = pip_value
        self.suit = suit
        if(card_type) == "Ace":
            self.low_pip_value=1         #used for Aces
            self.high_pip_value=11       #used for Aces
        self.card_image_surface = pygame.image.load(card_image).convert_alpha()
        self.rect = self.card_image_surface.get_rect(center = (1000,600))
   



