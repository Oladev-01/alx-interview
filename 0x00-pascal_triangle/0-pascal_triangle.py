#!/usr/bin/python3
from math import comb

"""this module creates a list of
integers representing pascal triangle
where the number of rows is parsed to the defined function"""


def pascal_triangle(n):
    """this function returns list of pascal triangle"""
    """ first of all if n <= 0: i return an empty list cos
    there row in pascal triangle begins from 0
    if n == 1, i return a list with an element of 1 cos in the
    pascal triangle, there is only 1 in the first row"""
    if n <= 0:
        return []
    if n == 1:
        return [1]
    pascal_triangle_list = []
    for row in range(n):
        # row serves as each row in the triangle
        nrow_list = []  # creating a new list for each row
        for col in range(row+1):
            # col serves as the col for each row
            nrow_list.append(comb(row, col))
        pascal_triangle_list.append(nrow_list)
    return pascal_triangle_list
