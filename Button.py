import pygame

class Button():
    def __init__(self,x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self, surface):
        action = False
        mouse_position = pygame.mouse.get_pos()

        #check if cursor collides with button and click condition
        if self.rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked==False:
                self.clicked = True
                action = True 
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw the button on the screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action #return the action if it is pressed or not
