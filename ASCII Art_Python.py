import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
t = t.upper()

characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '?']

print('Input value: ', file=sys.stderr)
print(t, file=sys.stderr)

positions = []
for i in t:
    try:
        ind = characters.index(i)
    except:
        positions.append( 26 )
    else:
        positions.append( ind )

print(positions, file=sys.stderr)

for i in range(h):
    row = input()
    
    my_row = ''
    for h in positions:
        for j in range(l):
            my_row += row[l*h + j]
    print(my_row)


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
