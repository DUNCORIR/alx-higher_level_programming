#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number (div).

    Args:
        matrix (list of lists): Matrix where each element is integer or float.
        div (int/float): Number by which to divide each element of matrix.

    Returns:
        list: New matrix with each element divided by div, rounded to 2 dec.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                    if each row of the matrix does not have the same size, or
                    if div is not a number.
        ZeroDivisionError: If div is 0.
    """

    if not (isinstance(matrix, list) and
            all(isinstance(row, list) for row in matrix)):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    if not (all(isinstance(element, (int, float))
            for row in matrix for element in row)):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    # Check if all rows have the same size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Div each element of matrix by div,round to 2 dcl then return new matrix
    return [[round(element / div, 2) for element in row] for row in matrix]
