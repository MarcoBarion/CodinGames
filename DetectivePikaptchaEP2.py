import sys
import math


# Functions
def find_start(maze):
    coordinates = [0, 0]
    for i in range(height):
        for j in range(width):
            if (maze[i][j] != 0 and maze[i][j] != '#'):
                coordinates[0] = i
                coordinates[1] = j
                return coordinates


def move(maze, direction, position):
    if (direction == '>'):
        position[1] += 1
        maze[position[0]][position[1]] += 1
    elif (direction == 'v'):
        position[0] += 1
        maze[position[0]][position[1]] += 1
    elif (direction == '<'):
        position[1] -= 1
        maze[position[0]][position[1]] += 1
    elif (direction == '^'):
        position[0] -= 1
        maze[position[0]][position[1]] += 1


def rotate(direction, rotation):
    directions = ['>', 'v', '<', '^']
    if (rotation == 'R'):
        return directions[(directions.index(direction) + 1) % 4]
    else:
        index = directions.index(direction)
        if (index == 0):
            return (directions[3])
        return directions[index - 1]


def find_movement_direction(maze, initial_direction, position, direction_rotation):
    if (initial_direction == '>' and
            maze[position[0]][position[1] + 1] != '#' and
            maze[position[0]][position[1] + 1] < len(maze[0])):
        return initial_direction
    elif (initial_direction == 'v' and
          maze[position[0] + 1][position[1]] != '#' and
          maze[position[0] + 1][position[1]] < len(maze)):
        return initial_direction
    elif (initial_direction == '<' and
          maze[position[0]][position[1] - 1] != '#' and
          maze[position[0]][position[1] - 1] >= 0):
        return initial_direction
    elif (initial_direction == '^' and
          maze[position[0] - 1][position[1]] != '#' and
          maze[position[0] - 1][position[1]] >= 0):
        return initial_direction
    else:
        initial_direction = rotate(initial_direction, direction_rotation)
        find_movement_direction(maze, initial_direction, position, direction_rotation)


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

width, height = [int(i) for i in input().split()]
initial_maze = []

for i in range(height):
    line = input()
    initial_maze.append(line)

side = input()

start_position = find_start(initial_maze)
direction = initial_maze[start_position[0]][start_position[1]]
position = start_position

maze = [['0'] * width for i in range(height)]
for i in range(height):
    for j in range(width):
        if (i == start_position[0] and j == start_position[1]):
            break
        else:
            maze[i][j] = initial_maze[i][j]

# Sizes
print("Width: ", file=sys.stderr)
print(width, file=sys.stderr)

print("Height: ", file=sys.stderr)
print(height, file=sys.stderr)

# Maze
print("\nInitial Maze:", file=sys.stderr)
for i in range(height):
    print(initial_maze[i], file=sys.stderr)

print( "\nType initial_maze", file=sys.stderr )
print( type(initial_maze), file=sys.stderr )
print( "\nType first and second cell", file=sys.stderr )
print( type(initial_maze[0][0]), file=sys.stderr )
print( type(initial_maze[0][1]), file=sys.stderr )

print("\nTransformed Maze:", file=sys.stderr)
for i in range(height):
    print(maze[i], file=sys.stderr)

print( "\nType maze", file=sys.stderr )
print( type(maze), file=sys.stderr )
print( "\nType first and second cell", file=sys.stderr )
print( type(maze[0][0]), file=sys.stderr )
print( type(maze[0][1]), file=sys.stderr )

# Wall Rule
print("\nWall to follow: " + side, file=sys.stderr)

# Starting Point
print("\nStarting Point: ", file=sys.stderr)
print(start_position, file=sys.stderr)

# Direction
print("\nDirection: ", file=sys.stderr)
print(direction, file=sys.stderr)

while True:

    find_movement_direction(maze, direction, position, side)
    move(maze, direction, position)

    # exit conditions
    if (start_position == position):
        break;

for i in range(height):
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    print(maze[i])
