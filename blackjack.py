import pygame
from sys import exit

FPS = 60
SCREEN_WIDTH= 1300
SCREEN_HEIGHT= 900

def run_game():
    #initialize pygame below
    pygame.init()
    
    #Font and color
    font = pygame.font.SysFont("arial", 80)
    text_color = (196,196,196)

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Black Jack")
    clock = pygame.time.Clock()

    #Start up the title menu
    screen.fill((0,132,113)) 
    title_image = font.render("Black Jack",True, text_color)
    screen.blit(title_image, (459,150))    
    print(title_image.get_width())

    #Game loop
    while True:
        



        #event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        clock.tick(FPS)