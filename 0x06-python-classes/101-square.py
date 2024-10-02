#!/usr/bin/python3
"""Module defines the Square class with size validation and printing."""


class Square:
    """Defines square with a private instance attribute size."""

    def __init__(self, size=0, position=(0, 0)):
        """initializes square with the given size and position."""
        self.size = size  # Use the setter to validate size
        self.position = position  # Use the setter to validate position

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method sets the position with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square and return it."""
        return self.__size * self.__size

    def my_print(self):
        """Print square using '#' character based on position"""
        if self.__size == 0:
            print("")  # prints an empty line.
            return

        [print("") for _ in range(self.__position[1])]

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        output = ""
        if self.__size == 0:
            return output

        output += "\n" * self.__position[1]
        for _ in range(self.__size):
            output += " " * self.__position[0] + "#" * self.__size + "\n"

        return output.rstrip()
