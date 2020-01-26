import pygame
import time
import random
from cell import *
from constants import *
from funcs import * 
from pygame.locals import *


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((canvas_width, canvas_width))
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
        # Game of Life runs here
        draw_grid(grid, screen)
        update_all_cells(grid)
        reset_new_cell_status(grid)
        pygame.display.update()


if __name__ == '__main__':
    main()
