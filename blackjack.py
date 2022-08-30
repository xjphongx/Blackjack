import pygame
from sys import exit

FPS = 60
SCREEN_WIDTH= 1300
SCREEN_HEIGHT= 900

def run_game():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Black Jack")
    clock = pygame.time.Clock()

    #Game loop
    while True:
        screen.fill((0,132,113))
        #event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        clock.tick(FPS)