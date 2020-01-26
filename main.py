import pygame
import time
import random
from pygame.locals import *

# Constants
grid_size = 70
canvas_width = 500
canvas_height = canvas_width
cell_size = canvas_width / grid_size
white = (255, 255, 255)
black = (0,  0,  0)


# My only, lonely class
class Cell:
    def __init__(self, x, y, pos):
        self.x = x
        self.y = y
        self.pos = pos
        self.status = False
        self.new_status = None
        if random.randint(0, 1) > .5:
            self.status = True

    def draw(self, screen):
        # rect = pygame.Rect((40, 290), (20, 20))
        color = white

        if self.status:
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

# Create the grid


def init_grid():
    grid = []
    for i in range(grid_size):
        _temp = []
        for j in range(grid_size):
            x = j * cell_size
            y = i * cell_size
            # For keeping track of its position on the grid
            pos = {
                'x': j,
                'y': i
            }
            _temp.append(Cell(x, y, pos))
        grid.append(_temp)
    return grid


def reset_new_cell_status(grid):
    for i in range(grid_size):
        for j in range(grid_size):
            grid[j][i].status = grid[j][i].new_status
            grid[j][i].new_status = None


def draw_grid(grid, screen):
    for i in range(grid_size):
        for j in range(grid_size):
            grid[j][i].draw(screen)

# Pygame


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Basic Pygame program')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Create the grid object
    grid = init_grid()

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        draw_grid(grid, screen)
        for i in range(grid_size):
            for j in range(grid_size):
                grid[j][i].update(grid)
        reset_new_cell_status(grid)
        pygame.display.update()


if __name__ == '__main__':
    main()
