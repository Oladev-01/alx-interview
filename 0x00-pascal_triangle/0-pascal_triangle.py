#!/usr/bin/python3
""" this module creates a list of
integers representing pascal triangle
where the number of rows is parsed to the defined function
"""


def factorial(n):
    """returns the factorial of a number"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def comb(row, col):
    """returns the combination of the numbers"""
    return factorial(row) // (factorial(row - col) * factorial(col))


def pascal_triangle(n):
    """this function returns list of pascal triangle
    first of all if n <= 0: i return an empty list cos
    there row in pascal triangle begins from 0
    if n == 1, i return a list with an element of 1 cos in the
    pascal triangle, there is only 1 in the first row"""
    if n <= 0:
        return []

    pascal_triangle_list = []
    for row in range(n):
        # row serves as each row in the triangle
        nrow_list = []  # creating a new list for each row
        for col in range(row+1):
            # col serves as the column for each row
            nrow_list.append(comb(row, col))
        pascal_triangle_list.append(nrow_list)
    return pascal_triangle_list
