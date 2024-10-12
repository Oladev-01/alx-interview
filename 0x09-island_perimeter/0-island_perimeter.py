#!/usr/bin/python3
"""calculating the perimeter of an island"""


def island_perimeter(grid):
    """function to calculate the perimeter of an island"""
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    if rows > 100 or cols > 100:
        return 0
    if rows == 0 or cols == 0:
        return 0
    perimeter = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # check above for water or out of bounds
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # check below
                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                # check the left
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # check the right
                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1
    return perimeter
