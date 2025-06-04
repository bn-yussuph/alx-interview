#!/usr/bin/python3
""" Rotate a matrix module
"""


def rotate_2d_matrix(matrix):
    """ Rotate a matrix by 90 degrees
    Args: A matrix to be rotated
    Return: None - rotata the matrix in place.
    """
    n = len(matrix)

    # Initialize a temp matrix
    res = [[0] * n for _ in range(n)]

    # Rotatae the matrix by 90 degrees
    for i in range(n):
        for j in range(n):
            res[j][n - i - 1] = matrix[i][j]

    # Copy the results back to the original matrix
    for i in range(n):
        for j in range(n):
            matrix[i][j] = res[i][j]
