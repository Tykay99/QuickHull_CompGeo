from CCW import Point
from CCW import CCW
import math
import sys

# Calculate the distance between a line ab and a point c
def distance(a, b, c):
    xa = a.getX()
    xb = b.getX()
    xc = c.getX()
    ya = a.getY()
    yb = b.getY()
    yc = c.getY()
    return abs((xc - xb) * (yb - ya) - (xb - xa) * (yc - yb)) / \
           math.sqrt(math.pow(xc - xb, 2) + math.pow(yc - yb, 2))

# Check whether point d is contained on triangle abc
def contained(a, b, c, d):
    first = CCW(a, b, d)
    second = CCW(b, c, d)
    third = CCW(c, a, d)
    # Check if d is on a line on the triangle
    if first == 0 or second == 0 or third == 0:
        return True
    # Check if d is inside of the triangle
    if first == second == third:
        return True
    return False

# Print points as desired
def ret(a):
    print(a.getX(), a.getY())

# Recursive function for points on top half of hull
def top(a, b, points):
    if len(points) == 0:
        return
    furthest = points[0]
    d = distance(a, b, furthest)
    # Find furthest points from line
    for i in points:
        if distance(a, b, i) > d:
            furthest = i
            d = distance(a, b, i)
    TopRight = []
    TopLeft = []
    # Consider and partition points outside of triangle a,b,furthest
    for i in points:
        if not contained(a, b, furthest, i):
            if i.getX() > furthest.getX():
                TopRight.append(i)
            elif i.getX() < furthest.getX():
                TopLeft.append(i)
    # Recursively call on TopLeft and TopRight, printing in middle
    # Such that ordering on vertices will be by increasing x coordinate
    top(a, furthest, TopLeft)
    ret(furthest)
    top(furthest, b, TopRight)

# Recursive function for points on bottom half of hull
def bottom(a, b, points):
    if len(points) == 0:
        return
    furthest = points[0]
    d = distance(a, b, furthest)
    # Find furthest points from line
    for i in points:
        if distance(a, b, i) > d:
            furthest = i
            d = distance(a, b, i)
    BottomRight = []
    BottomLeft = []
    # Consider and partition points outside of triangle a,b,furthest
    for i in points:
        if not contained(a, b, furthest, i):
            if i.getX() > furthest.getX():
                BottomRight.append(i)
            elif i.getX() < furthest.getX():
                BottomLeft.append(i)
    # Recursively call on BottomRight and BottomLeft, printing in middle
    # Such that ordering on vertices will be by increasing x coordinate
    bottom(furthest, b, BottomRight)
    ret(furthest)
    bottom(a, furthest, BottomLeft)

def quickhull(Points):
    # Calculate mins and maxes
    Xmax = Xmin = Points[0]
    Ymin = Ymax = Point(math.inf, math.inf)
    for i in Points:
        if i.getX() < Xmin.getX():
            Xmin = i
        if i.getX() > Xmax.getX():
            Xmax = i
    Top = []
    Bottom = []
    # Partition top and bottom points
    for i in Points:
        if CCW(Xmin, Xmax, i) == -1:
            Top.append(i)
        elif CCW(Xmin, Xmax, i) == 1:
            Bottom.append(i)
    Ydis = -math.inf
    # Calculate furthest points above and below from line Xmin,Xmax
    for i in Top:
        if distance(Xmin, Xmax, i) > Ydis:
            Ymax = i
            Ydis = distance(Xmin, Xmax, i)
    Ydis = -math.inf
    for i in Bottom:
        if distance(Xmin, Xmax, i) > Ydis:
            Ymin = i
            Ydis = distance(Xmin, Xmax, i)
    TopRight = []
    TopLeft = []
    BottomRight = []
    BottomLeft = []
    # Only consider those points outside the quadrilateral
    # Partition Top and Bottom to get four arrays for recursive function calling
    for i in Top:
        if Ymax.getX() != math.inf and not contained(Xmin, Xmax, Ymax, i):
            if i.getX() > Ymax.getX():
                TopRight.append(i)
            elif i.getX() < Ymax.getX():
                TopLeft.append(i)
    for i in Bottom:
        if Ymin.getX() != math.inf and not contained(Xmin, Xmax, Ymin, i):
            if i.getX() > Ymin.getX():
                BottomRight.append(i)
            elif i.getX() < Ymin.getX():
                BottomLeft.append(i)
    # Check all four corners, in proper order, for printing
    # With increasing x coordinates
    ret(Xmin)
    top(Xmin, Ymax, TopLeft)
    if Ymax.getX() != math.inf:
        ret(Ymax)
    top(Ymax, Xmax, TopRight)
    ret(Xmax)
    bottom(Ymin, Xmax, BottomRight)
    if Ymin.getX() != math.inf:
        ret(Ymin)
    bottom(Xmin, Ymin, BottomLeft)

def main():
    arr = []
    for l in sys.stdin:
        arr += l.strip().split()
    first_int = int(arr[0])
    curr = 1
    for i in range(0, first_int):
        Points = []
        second = int(arr[curr])
        curr = curr + 1
        for j in range(curr, curr + second * 2, 2):
            point = Point(arr[j], arr[j + 1])
            Points.append(point)
        quickhull(Points)
        print("\n")
        curr = curr + second * 2

if __name__ == "__main__":
    main()