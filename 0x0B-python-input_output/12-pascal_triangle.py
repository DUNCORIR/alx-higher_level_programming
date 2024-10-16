#!/usr/bin/python3
"""
The module contains function to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle of height n.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:  # handle base case
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate each row from 2 to n
    for row in range(1, n):
        new_row = [1]  # Start the new row with 1

        # Calculate middle elements (sum pairs from previous row)
        for i in range(1, row):
            new_element = triangle[row - 1][i - 1] + triangle[row - 1][i]
            new_row.append(new_element)

        new_row.append(1)  # End row with 1
        triangle.append(new_row)  # Append the new row to the triangle

    return triangle  # Completed triangle.
