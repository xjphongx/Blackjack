
from scripts.gameboard import Gameboard
from scripts.state import State

class Loading(State):
    def __init__(self, game):
        super().__init__(game)

    def render(self, display):
        display.fill(self.game.background_color)
        self.game.draw_text("Loading screen...", 
            70, 
            self.game.display_width/2,
            self.game.display_height/2)

    def update(self, actions):
        self.exit_state() #leaves the loading state
        next_state = Gameboard(self.game)
        next_state.enter_state()