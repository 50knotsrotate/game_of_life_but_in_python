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

    def draw(self, screen):
        rect = pygame.Rect((40, 290), (20, 20))
        color = white
        if self.status == True:
            color = black
        pygame.draw.rect(screen, color, (self.x, self.y, cell_size, cell_size))
    
    def update(self, grid):
        live_cells = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if grid[(self.pos['y'] + i + grid_size) % grid_size][(self.pos['x'] + j + grid_size) % grid_size].status:
                    live_cells = live_cells + 1
        if self.status == True:
            live_cells = live_cells - 1
            if live_cells == 2 or live_cells == 3:
                self.new_status = True
            else:
                self.new_status = False
        else:
            if live_cells == 3:
                self.new_status = True
            else:
                self.new_status = False
            
