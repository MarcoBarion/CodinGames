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
    
def can_move(maze, pos_x, pos_y):
    if maze[pos_x][pos_y] == "#":
        return False
    
    returt True

def move(maze, direction):
    move_dic = 

w, h = [int(i) for i in input().split()]
n = int(input())

maze = []

for i in range(h):
    line = input()
    maze.append(line)
    
print(maze)
