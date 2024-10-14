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
