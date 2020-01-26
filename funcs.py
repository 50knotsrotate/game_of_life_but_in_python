import pygame
from cell import Cell
from constants import *

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

# def draw_grid(grid):
#     for i in range(grid_size):
#         for j in range(grid_size):
#             grid[j][i].draw()



