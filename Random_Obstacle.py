
from vpython import *
import random

# Define the dimensions of the chess board
square_size = 1

# Generate random coordinates for the obstacles
def generate_obstacle_coordinates(num_obstacles,n):
    x=(n//2)+1
    obstacle_coords = []
    for i in range(num_obstacles):
        coord = (random.randint(1, n)-x, 0, random.randint(1, n)-x)
        obstacle_coords.append(coord)
    return obstacle_coords

# Draw the chess board
'''def draw_chess_board():
    for i in range(n):
        for j in range(n):
            if (i+j) % 2 == 1:
                sColor = color.black
            else:
                sColor = color.white
            box(pos=vector(i+0.5,0.1,j+0.5), length=1, height=0.1, width=1, color=sColor)'''

# Draw the obstacles on the chess board
'''def draw_obstacles(obstacle_coords):
    for i, coord in enumerate(obstacle_coords):
        # if i == 0:
        #     obstacle_color = color.red
        # elif i == 1:
        #     obstacle_color = color.green
        # elif i == 2:
        #     obstacle_color = color.blue
        # else:
        obstacle_color = color.yellow
        sphere(pos=vector(coord[0] * square_size + 0.5, coord[1] * square_size, coord[2] * square_size + 0.5),
               radius=0.4 * square_size, 
               color=obstacle_color)'''

# Get user input for number of obstacles
#num_obstacles = n

# Generate random obstacle coordinates
#obstacle_coords = generate_obstacle_coordinates(num_obstacles)

# Create a 3D scene using Vpython
#scene = canvas(title='Chess Board', width=800, height=800)

# Draw the chess board
#print(obstacle_coords)
# Draw the obstacles on the chess board

