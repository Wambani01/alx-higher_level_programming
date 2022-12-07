#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        row_matrix = []
        for element in row:
            row_matrix.append(element)
        new_matrix.append(row_matrix)
    return new_matrix
