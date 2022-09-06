from turtle import title
import pygame
from sys import exit

from scripts.button import Button
from scripts.gameboard import GameBoard

FPS = 60
SCREEN_WIDTH= 1300
SCREEN_HEIGHT= 900

def run_game():
    #initialize pygame below
    pygame.init()
    
    
    #Font and color
    font = pygame.font.SysFont("arial", 160)
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
    back_image = pygame.image.load("images/buttons/back_button.png").convert_alpha()
    back_button = Button(50,25,back_image,.10)
    #next_image = pygame.image.load("images/buttons/next_button.png").convert_alpha()
    #next_button = Button(1050,25,next_image, .10)
   

    #menu bool variables
    is_menu_screen = True
    is_game_screen = False
    is_how_to_play_screen = False
    is_paused_screen = False

    #Game loop
    while True:
        
        #start up the main menu first
        screen.fill((0,132,113)) 
        title_image = font.render("Black Jack",True, text_color)
        screen.blit(title_image, (280,75))


        #click menu button functionality
        if is_menu_screen:
            if play_game_button.draw(screen):
                #go to gameboard
                is_game_screen = True
                is_menu_screen = False
            if how_to_play_button.draw(screen):
                #go to playing instruction screen
                is_menu_screen = False
                is_how_to_play_screen = True
            if quit_button.draw(screen):
                pygame.quit()
                exit()

        #go to this screen if the how to play button is pressed
        if is_how_to_play_screen:
            screen.fill((0,132,113))
            #if this button is click, go back to menu screen
            if back_button.draw(screen):
                is_menu_screen = True
                is_how_to_play_screen = False

        #go to this screen if play game button is pressed
        if is_game_screen:
            screen.fill((0,132,113))
            gameboard = GameBoard()
            gameboard.play()






        #event handlers
        for event in pygame.event.get():
            #event for pressing keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  #esc key button for pause
                    #pause game
                    pass

            
            #close game if player clicks top right
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        clock.tick(FPS)