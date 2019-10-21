import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def opposite(parentesis):
    if parentesis == '{':
        return '}'
    elif parentesis == '[':
        return ']'
    elif parentesis == '(':
        return ')'
    else:
        raise Exception('Input symbol not reconised')


expression = input()

print(expression, file=sys.stderr)
li = list(expression)
print(li, file=sys.stderr)

open_p = ['(','[','{']
closed_p = [')',']','}']

open_index = -1
closed_index = -1

modified = True
while modified:
    modified = False
    
    for i in li:
        if i in open_p:
            open_index = li.index(i)
        elif i in closed_p:
            if i == opposite( li[open_index] ):
                closed_index = li.index(i)
                li[open_index] = 0
                li[closed_index] = 0
                modified = True
                break
    
    


if '(' in li or ')' in li or '[' in li or ']' in li or '{' in li or '}' in li:
    print('false')
else:
    print('true')


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
