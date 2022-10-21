# Implementation of QuickHull Algorithm and CCW algorithm

INPUT:

The first line of the input contains one integer n, the number of test cases for CCW.

Each of the following n lines contains 6 floating point numbers separated by spaces (x_A is the x coordinate of point A etc.):
x_A y_A x_B y_B x_C y_C

The next line of the input contains one integer m, which is the number of test cases for segment intersection.

Each of the following m lines contains 8 floating point numbers separated by spaces (A-B is the first line segment, C-D is the second line segment):

x_A y_A x_B y_B x_C y_C x_D y_D


OUTPUT: 

Print n lines with n answers to the CCW test cases in each line.

Print an empty line (or any kind of separation).

Print m lines with m answers to the line segment intersection test cases in each line.



---------- Problem 3 ----------

INPUT:

The first line contains one integer n, the number of test cases (We may ask you to compute more than 1 convex hulls).

The test cases are giving in the following lines, each test case has the following format:
- a line containing one integer m, which is the number of points.
- Each of the following m lines contain 2 floating point numbers (x, y coordinates of the point) separated by spaces:
x_i y_i


OUTPUT:

When you output the vertices of a convex hull, each line should contain 2 floating point numbers, separated by space:

x_i y_i

To make life easier, please start from the leftmost vertex, and output in a clockwise manner.

If n > 1, print some kind of separation between different convex hulls.



