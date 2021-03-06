#!/usr/bin/env checkio --domain=py run three-points-circle

# Nicola discovered a calliper inside a set of drafting tools he received as
# a gift.    Seeing the caliper, he has decided to learn how to use it.
# 
# Through any three points that do not exist on the same line, there lies a
# unique circle.    The points of this circle are represented in a string
# with the coordinates like so:
# 
# 
#     "(x1,y1),(x2,y2),(x3,y3)"
# 
# Wherex1,y1,x2,y2,x3,y3are digits.
# 
# You should find the circle for three given points, such    that the circle
# lies through these point and return the result as a string    with the
# equation of the circle.    In a Cartesian coordinate system (with an X and
# Y axis),    the circle with central coordinates of (x0,y0) and radius of r
# can be described with the following equation:
# 
# 
#     "(x-x0)^2+(y-y0)^2=r^2"
# 
# wherex0,y0,rare decimal numbers rounded totwo decimal points.    Remove
# extraneous zeros and all decimal points, they are not necessary.    For
# rounding, use the standard mathematical rules.
# 
# 
# 
# Input:Coordinates as a string..
# 
# Output:The equation of the circle as a string.
# 
# Precondition:All three given points do not lie on one line.
# 0 < xi, yi, r < 10
# 
# 
# END_DESC

import re
from math import hypot


def checkio(data: str):
    # extract points coordinates from the string
    pointsRegex = re.compile(r'\(...\)')
    points = pointsRegex.findall(data)
    A, B, C = map(eval, points)

    # TODO: check whether not on one line and if three different points

    # middle of line |AB| segment
    midAB = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
    midBC = ((B[0] + C[0]) / 2, (B[1] + C[1]) / 2)

    # vector of |AB|
    vectAB = (B[0] - A[0], B[1] - A[1])
    vectBC = (C[0] - B[0], C[1] - B[1])

    # get a, b from respective vectors
    aAB = vectAB[0]
    bAB = vectAB[1]

    aBC = vectBC[0]
    bBC = vectBC[1]

    # solve for c in 'ax + by + c = 0' in middle |AB|
    cAB = -aAB * midAB[0] - bAB * midAB[1]
    cBC = -aBC * midBC[0] - bBC * midBC[1]

    # solve for x in '(-aABx - cAB) / bAB = (-aBCx - cBC) / bBC'
    x = (bBC * cAB - bAB * cBC) / (bAB * aBC - bBC * aAB)

    if bAB != 0:
        y = (-aAB * x - cAB) / bAB
    elif bBC != 0:
        y = (-aBC * x - cBC) / bBC

    # calculate radius r ( |A[x,y]| = |B[x,y]| = |C[x,y]| )
    r = hypot(A[0] - x, A[1] - y)

    return f'(x-{round(x, 2):.5g})^2+(y-{round(y, 2):.5g})^2={round(r, 2):.5g}^2'


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"

print(checkio("(7,3),(9,6),(3,6)"))
print(checkio("(3,4),(6,6),(4,8)"))