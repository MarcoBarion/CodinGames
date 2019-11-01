import math
import sys


def find_initial_position(maze, w, h):
    for i in range(0, h):
        for j in range(0,w):
            if maze[i][j] == "O":
                return [i, j]
    
    return -1


def can_move(maze, direction, x, y):
    
    if direction == "U":
        if maze[ x -1 ][ y ] == "#":
            return False
    elif direction == "R":
        if maze[ x ][ y + 1 ] == "#":
            return False
    elif direction == "D":
        if maze[ x +1 ][ y ] == "#":
            return False
    elif direction == "L":
        if maze[ x ][ y-1 ] == "#":
            return False
        
    return True


def turn_clockwise(direction):
    directions = ["U", "R", "D", "L"]
    return directions[ (directions.index(direction) + 1) % 4 ]


def move(direction, coordinates):
    if direction == "U":
        coordinates[0] -=1
    elif direction == "R":
        coordinates[1] +=1
    elif direction == "D":
        coordinates[0] +=1
    elif direction == "L":
        coordinates[1] -=1


def main():
    w, h = [int(i) for i in input().split()]
    n = int(input())
    
    maze = []
    direction = "U"
    position = [0, 0]
    my_log = []
    
    for i in range(h):
        line = input()
        maze.append(line)
        
    position = find_initial_position(maze, w, h)
    my_log.append( [position[0], position[1], direction] )
    
    for i in range(0, n):
        while not can_move(maze, direction, position[0], position[1]):
            direction = turn_clockwise(direction)
            
        move(direction, position)
        if [position[0], position[1], direction] in my_log:
            loop = my_log[ my_log.index([position[0], position[1], direction]) : ]
            position = loop[ (n-i-1) % len(loop) ][0:2]
            break
        else:
            my_log.append( [position[0], position[1], direction] )
    
    print( "%(x)d %(y)d" %{"x": position[1], "y": position[0]} )


main()
