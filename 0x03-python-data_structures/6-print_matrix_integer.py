#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Check if matrix is empty or contains only empty lists
    if matrix == [[]]:
        return
    # Loop through each row in the matrix
    for row in matrix:
        # Create a variable to store the formatted row
        formatted_row = ""
        # Loop through each element in the row
        for idx, element in enumerate(row):
            if idx != len(row) - 1:
                formatted_row += "{} ".format(element)
            else:
                formatted_row += "{}".format(element)
    # Print the formatted row
    print(formatted_row)
