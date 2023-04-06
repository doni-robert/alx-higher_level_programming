#!/usr/bin/python3
"""matrix_divided module"""


def matrix_divided(matrix, div):
    """
    Divides all elments of a matrix by a number div

    Args:
        matrix(list of list of ints or floats): the matrix whose
            elements are to be divided
        div(int or float): The divisor

    Returns:
        A new matrix with the quotients

    Raises:
        TypeError: if matrix is not a list of integers or floats
            or if the rows of the matrix are not all of the same size
            or if div is not a number.
        ZeroDivisionError: if div is equal to zero
    """
    new_matrix = [[]]
    row_len = len(matrix[0])

    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

        for r in row:
            if (not isinstance(r, int) and not isinstance(r, float)):
                raise TypeError("matrix must be a matrix(list of lists) \
                        of integers/floats")
    new_matrix = [list(map(lambda r: round(r / div, 2), row))for row in matrix]
    return new_matrix
