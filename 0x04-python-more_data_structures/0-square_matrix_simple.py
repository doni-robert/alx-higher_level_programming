#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    for r in matrix:
        new_matrix = list(map((lambda x: x ** 2), r))
    return new_matrix
