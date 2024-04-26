#!/usr/bin/python3
"""Module that contains matrix function"""


def rotate_2d_matrix(matrix):
    """rotate the matrix clockwise (90 degrees)"""
    ziped = zip(*reversed(matrix))
    for column1, column2 in enumerate(ziped):
        matrix[column1] = list(column2)
