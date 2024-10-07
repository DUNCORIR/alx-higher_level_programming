#!/usr/bin/python3

"""
A module that defines a rectangle class.
"""


class Rectangle:
    """Represents a rectangle with width and height.

    Public class attribute:
        number_of_instances: Keeps track of the number of Rectangle instances
        print_symbol: Symbol used for string representation.
    """

    # Public class attributes
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.height = height  # Calls the width setter
        self.width = width  # Calls the height setter
        Rectangle.number_of_instances += 1  # Increment the class attribute

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle with validation.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value  # Initialize the private attribute

    @property
    def height(self):
        """# Initialize the private attribute

        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle with validation.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value  # Initialize the private attribute

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int : The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
        int: The perimeter of tghe rectangle.
        Returns 0 if width or height.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the
        rectangle using '#' character.

        Returns:
            str: the rectangle as astring of '#' charactrs.
        """
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)
        return '\n'.join([symbol * self.width for _ in range(self.height)])

    def __repr__(self):
        """Returns a formal string representation of the rectangle.

        Returns:
            str: string representation of the rectangle
            to be able to recreate a new instance using eval().
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Prints a message when the rectangle instance is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement the class attribute

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the Rectangle with the bigger area, or rect_1 if equal.

        Args:
            rect_1 (Rectangle): First rectangle to compare.
            rect_2 (Rectangle): Second rectangle to compare.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: The rectangle with the bigger area, or rect_1 if equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
