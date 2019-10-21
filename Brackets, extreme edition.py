import sys
import math


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
    open_index = -1
    closed_index = -1
    
    for i in range(len(li)):
        if li[i] in open_p:
                open_index = i
        elif li[i] in closed_p:
            if open_index != -1 and li[i] == opposite( li[open_index] ):
                closed_index = i
                li[open_index] = '0'
                li[closed_index] = '0'
                modified = True
            
            break
    
    print(li, file=sys.stderr)


if '(' in li or ')' in li or '[' in li or ']' in li or '{' in li or '}' in li:
    print('false')
else:
    print('true')
