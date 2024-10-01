#!/usr/bin/python3
"""
A class that defines a square.
"""


class Square:
    """
    The class defines Square by its size.
    """

    def __init__(self, size):
        """
        Initialize the square with a specific size.


        Args:
            size (int): The size of the square.
        """
        self.__size = size  # private instance attribute.
