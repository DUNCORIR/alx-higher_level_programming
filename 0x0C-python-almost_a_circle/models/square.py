#!/usr/bin/python3
""" A class square that inherits from Rectangle."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the square instance.

        Args:
            size (int): the size of the square (both width and height).
            x (int): The x position of the square.
            y (int): The y position of the square
            id (int): The id of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set size of square, updating both width and height."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Overrides __str__ method to provide a custom string reprentation."""
        return (
                "[Square] ({}) {}/{} - {}".format(
                    self.id, self.x, self.y, self.width)
            )
