import pygame
from sys import exit

from Button import Button

FPS = 60
SCREEN_WIDTH= 1300
SCREEN_HEIGHT= 900

def run_game():
    #initialize pygame below
    pygame.init()
    
    #Font and color
    font = pygame.font.SysFont("arial", 80)
    text_color = (225,228,230)

    #Start screen
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Black Jack")
    clock = pygame.time.Clock()

    

    #loading button images and create button instances
    play_game_image = pygame.image.load("images/buttons/play_game_button.png").convert_alpha()
    play_game_button = Button(510,250, play_game_image, .15)
    how_to_play_image = pygame.image.load("images/buttons/how_to_play_button.png").convert_alpha()
    how_to_play_button = Button(510,350, how_to_play_image, .15)
    quit_image = pygame.image.load("images/buttons/quit_button.png").convert_alpha()
    quit_button = Button(510, 450, quit_image, .15)


    #Start up the title menu
    screen.fill((0,132,113)) 
    title_image = font.render("Black Jack",True, text_color)
    screen.blit(title_image, (459,150))    
    play_game_button.draw(screen)
    how_to_play_button.draw(screen)
    quit_button.draw(screen)



    #Game loop
    while True:
        
        



        #event handlers
        for event in pygame.event.get():
            #event for pressing keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  #esc key button for pause
                    #pause game
                    pass

            
            
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        clock.tick(FPS)