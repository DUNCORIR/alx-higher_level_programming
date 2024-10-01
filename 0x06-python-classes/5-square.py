#!/usr/bin/python3
"""Module defines the Square class with size validation and printing."""


class Square:
    """Defines square with a private instance attribute size."""

    def __init__(self, size=0):
        """initializes square with the given size."""
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method sets the size with validation.

        Args:
            value (int): New size for the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square and return it."""
        return self.__size * self.__size

    def my_print(self):
        """Print square using '#' character.

        if size is zero then print an empty line.
        """
        if self.__size == 0:
            print("")  # prints an empty line.
        else:
            for _ in range(self.__size):
                print("#" * self.__size)  # Print a row of '#' characters.
