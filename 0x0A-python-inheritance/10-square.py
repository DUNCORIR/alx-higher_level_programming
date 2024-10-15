#!/usr/bin/python3
"""
The module defines A base class for geometry objects.
"""


class BaseGeometry:
    """
    A base class for geometry objects.
    """

    def area(self):
        """
        Method that raises an exception when called
        because it is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer.

        Args:
        name: always a string, representing name of variable.
        value: The value to validate.

        Raises:
        TypeError: If 'value' is not integer
        valueError: if 'value' is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Represents a rectangle, inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes the Rectangle with width and height.

        Arguments:
        width: width of the rectangle, validated as a positive integer.
        height: height of the rectangle, validated as a positive integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the rectangle description
        in the format [Rectangle] <width>/<height>.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Represents a square, inherits from Rectangle."""

    def __init__(self, size):
        """Initializes the Square with size.

        Args:
        size -- The size of the square, validated as a positive integer.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Returns the square description in the format
        [Square] <size>/<size>.
        """
        return f"[Square] {self.__size}/{self.__size}"
