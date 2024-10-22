#!/usr/bin/python3
"""The module has Rectangle class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    # Class constructor
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x position of the rectangle.
            y (int): The y position of the rectangle.
            id (int): The id of rectangle inherited from Base.
        """
        super().__init__(id)  # Calling constructor of Base class.
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getter and Setter for width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # Getter and Setter for height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # Getter and Setter for x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # Getter and Setter for y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and return area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the rectangle using '#' character."""
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """Overrides __str__ method and return a represented string."""
        return (
            "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height
            )
        )
