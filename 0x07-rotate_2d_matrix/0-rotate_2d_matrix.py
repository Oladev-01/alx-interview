#!/usr/bin/python3
"""rotating 2D matrix"""
from typing import List


def rotate_2d_matrix(matrix: List[List]) -> List[List]:
    """rotating 2D matrix"""
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for f in range(n):
        matrix[f].reverse()
