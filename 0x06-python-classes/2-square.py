#!/usr/bin/python3
"""
A class that defines a square with size validation.
"""


class Square:
    """
    The class defines a square by its size.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a specific size.


        Args:
            size (int): The size of the square, must be an integer >=0.

        Raises:
            TypeError: If size is not integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):  # Check if size is an integer
            raise TypeError("size must be an integer")
        if size < 0:  # checking if size is < 0.
            raise ValueError("size must be >= 0")

        self.__size = size  # Private instance attribute
