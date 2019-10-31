import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def find_initial_position(maze, w, h):
    for i in range(0, h):
        for j in range(0,w):
            if maze[i][j] == "O":
                return [i, j]
    
    # For now it returns -1 try to implement with exceptions
    return -1

# INPUT:
# maze: list 2 dimensions
# coordinates: list 2 values
def can_move(coordinates, direction):
    tmp_coordinates = coordinates[:]
    tmp_coordinates = move(direction, tmp_coordinates)
    if maze[ tmp_coordinates[0] ][ tmp_coordinates[1] ] == "#":
        return False
    
    return True

def turn_clockwise(direction):
    directions = ["U", "R", "D", "L"]
    return directions[ (directions.index(direction) + 1) % 4 ]

# INPUT:
# maze
# direction
# coordinates
#
# OUTPUT:
# coordinates: list of coordinates
#
# N.B. there is probably no need of a return, when you modify coordinates this already modify the object in memory
def move(direction, coordinates):
    if direction == "U":
        coordinates[0] -=1
    elif direction == "R":
        coordinates[1] +=1
    elif direction == "D":
        coordinates[0] +=1
    elif direction == "L":
        coordinates[1] -=1
    
    return coordinates
    

w, h = [int(i) for i in input().split()]
n = int(input())

maze = []
direction = "U"
position = [0, 0]

for i in range(h):
    line = input()
    maze.append(line)
    
position = find_initial_position(maze, w, h)

for i in range(0, n):
    # We are not taking care of the case that the guy can not rotate more than once
    if not can_move(position, direction):
        direction = turn_clockwise(direction)
    position = move(direction, position)

print( "%(x)d %(y)d" %{"x": position[1], "y": position[0]} )

