#test player and dealer on a board with gameboard instances
#from turtle import end_fill
from scripts.player import Dealer,Player
from scripts.card import Card
from scripts.hand import Hand
import json
import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
display = pygame.Surface((500,500))
clock = pygame.time.Clock()



templist = [0,1,2,3,4,5,6]
print(templist[:-1])
templist = templist[:-1] #everything until the last 
print(templist)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(display,(0,0))
    pygame.display.update()
    clock.tick(60)
      
        






