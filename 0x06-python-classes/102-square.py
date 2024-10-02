#!/usr/bin/python3

"""The module defines the Square class with setter, comparison and getter"""


class Square:
    """Defines a square with private instance attribute size."""

    def __init__(self, size=0):
        """Initializes square with the given data."""
        self.size = size  # Use setter for validating

    @property
    def size(self):
        """Getter method for size retrieval."""
        return self.__size

    @size.setter
    def size(self, value):
        """ setter method for setting size with validation.

        Args:
            value (ifloat/int): New size for the square.

        Raises:
            TypeError: if size is not integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates area of the square and return it."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Equality comparison based on square area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparison based on square area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparison based on square area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison based on square area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparison based on square area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison based on square area."""
        return self.area() >= other.area()
