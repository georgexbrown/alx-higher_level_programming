#!/usr/bin/python3

"""Defines a function that returns the Pascal's Triangle representation"""


def pascal_triangle(n):
    """Returns a list of lists of integer representing pascal's triangle
    Args:
        n: integer to determine list
    """

    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
