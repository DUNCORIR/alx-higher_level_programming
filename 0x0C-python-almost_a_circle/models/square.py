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

    def __str__(self):
        """Overrides __str__ method to provide a custom string reprentation."""
        return (
                "[Square] ({}) {}/{} - {}".format(
                    self.id, self.x, self.y, self.width)
            )
