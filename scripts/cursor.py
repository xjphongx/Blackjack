import pygame


class Cursor():
    def __init__(self):
        self.chip_stack = []
        self.mouse_position = pygame.mouse.get_pos()

