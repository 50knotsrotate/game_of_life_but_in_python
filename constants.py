# Change this to see the simulation with a different amount of cells
# Any whole number will work, but after 100 it starts tog et really slow. Use caution.
grid_size = 75

# Size of pygame window. Less than 100 is not ideal.
canvas_width = 500

# This is how each cell knows how big to make itself.
cell_size = canvas_width / grid_size

# RGB values for colors. Go crazy, just make sure they are not the same. 
white = (255, 255, 255)
black = (0,  0,  0)
