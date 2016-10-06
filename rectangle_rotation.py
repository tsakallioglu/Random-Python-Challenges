#A rectangle with sides equal to even integers a and b is drawn on the Cartesian plane. 
#Its center (the intersection point of its diagonals) coincides with the point (0, 0), 
#but the sides of the rectangle are not parallel to the axes; instead, they are forming 45 degree angles with the axes.
#How many points with integer coordinates are located inside the given rectangle (including on its sides)?

from math import sqrt
def rectangleRotation(a, b):
    x= int((a/2)/(sqrt(2)/2))
    y= int((b/2)/(sqrt(2)/2))

    result=(x+1)*(y+1) + x*y
    if result%2==0:
        return result-1
    else:
        return result
