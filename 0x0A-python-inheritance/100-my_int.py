#!/usr/bin/python3
"""
Module contains class MyInt, that inherits from int
and inverts the behaviour of == and != operators.
"""


class MyInt(int):
    """
    MyInt is subclass of int that inverts
    behaviour of == and != operators.
    """
    def __eq__(self, other):
        """
        Override the == operator to invert its behavior.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the != operator to invet its behavior.
        """
        return super().__eq__(other)
