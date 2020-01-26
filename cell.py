import random
import pygame
from constants import *
class Cell:
    def __init__(self, x, y, pos):
        self.x = x
        self.y = y
        self.pos = pos
        self.status = False
        if random.randint(0, 1) > .5:
            self.status = True

    def draw(self):
        rect = pygame.Rect((40, 290), (20, 20))
        color = white
        if self.status == True:
            color = black
        pygame.draw.rect(screen, color, (self.x, self.y, cell_size, cell_size))
            
