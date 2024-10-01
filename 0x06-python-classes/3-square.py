#!/usr/bin/python3
"""Module that defines the Square class."""


class Square:
    """Defines a square with a private instance attribute 'size'"""

    def __init__(self, size=0):
        """
        Initializes square with given size.
        Args:
            size (int): Size of square's side. Default = 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: if size less than zero.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of square and return.
        Returns:
            int: Area of square.
        """
        return self.__size * self.__size
