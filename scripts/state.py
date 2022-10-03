
#Abstract data class
class State():
    def __init__(self, game):
        self.game = game #reference to the game class
        self.prev_state = None
        self.center_width = self.game.display_width/2
        self.center_height = self.game.display_height/2
        self.run_display = True

    def update(self):
        pass
    def render(self, surface):
        pass

    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self) #add the object into stack

    def exit_state(self):
        self.game.state_stack.pop()








