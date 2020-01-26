from constants import *
from cell import Cell
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

def update_all_cells(grid):
     for i in range(grid_size):
        for j in range(grid_size):
            grid[j][i].update(grid)
            
def reset_new_cell_status(grid):
    for i in range(grid_size):
        for j in range(grid_size):
            grid[j][i].status = grid[j][i].new_status
            grid[j][i].new_status = None


def draw_grid(grid, screen):
    for i in range(grid_size):
        for j in range(grid_size):
            grid[j][i].draw(screen)
