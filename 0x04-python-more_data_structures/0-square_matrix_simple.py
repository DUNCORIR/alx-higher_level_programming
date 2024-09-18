#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []  # initialize empty list for new matrix
    for row in matrix:  # Iterate through each row of the matrix
        squared_row = []  # New list to store the squared values of row
        # Iterate through each element in the row.
        for element in row:
            #  Square element and append it into square_row.
            squared_row.append(element ** 2)
        new_matrix.append(squared_row)
    # Return the new matrix
    return new_matrix
