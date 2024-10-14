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
