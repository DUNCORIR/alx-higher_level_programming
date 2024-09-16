#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Check if the matrix contains any rows to print
    for row in matrix:
        # Use ' '.join() to print the integers on the same line
        print(" ".join("{:d}".format(element) for element in row))
