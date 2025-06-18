#!/usr/bin/python3
""" Module for finding island perimeter
"""


def island_perimeter(grid):
    """ Afxn for island perimeter
        Args: a grid
        Returnd: the perimeter
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                # chech top neighbor
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 1

                # check bottom neighbor
                if r < rows - 1 and grid[r + 1][c] == 1:
                    perimeter -= 1

                # check left neighbor
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 1

                # check right neighbor
                if c < cols - 1 and grid[r][c + 1] == 1:
                    perimeter -= 1
    return perimeter
