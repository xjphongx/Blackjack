#from scripts.blackjack import run_game
from scripts.game import Game

#Main function will intialize the game 
def main():    
    #start the gameS
    #run_game()
    game = Game()
    while game.running:
        game.playing=True
        game.game_loop()





if __name__ == '__main__':
    main()