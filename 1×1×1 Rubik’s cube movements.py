import sys
import math

rotations = input()
face_1 = input()
face_2 = input()

def rotate( face, rotation):
    x_l = [ 'U', 'B', 'D', 'F' ]
    y_l = [ 'F', 'L', 'B', 'R' ]
    z_l = [ 'U', 'R', 'D', 'L' ]
    
    if rotation == "x":
        if face in x_l:
            return x_l[ (x_l.index(face) + 1) % 4]
    elif rotation == "x'":
        if face in x_l:
            return x_l[ x_l.index(face)-1 ]
            
    elif rotation == "y":
        if face in y_l:
            return y_l[ (y_l.index(face)+1)%4 ]
    elif rotation == "y'":
        if face in y_l:
            return y_l[ y_l.index(face)-1 ]
            
    elif rotation == "z":
        if face in z_l:
            return z_l[ (z_l.index(face) +1) % 4 ]
    elif rotation == "z'":
        if face in z_l:
            return z_l[ z_l.index(face)-1 ]
    
    return face
        

rotations_l = rotations.split(' ')

for r in rotations_l:
   face_1 = rotate( face_1, r )
   face_2 = rotate( face_2, r )

print(face_1)
print(face_2)
