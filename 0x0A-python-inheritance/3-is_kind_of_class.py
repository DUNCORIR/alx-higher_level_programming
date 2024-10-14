#!/usr/bin/python3
"""
The module has function that checks if object is an instance
of or if the object is an instance of class it inherited from.
"""


def is_kind_of_class(obj, a_class):
    """
    The function checks if object is an instance of the instsnce
    of class it inherited from.

    Args:
        obj: The object to check
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or of class that it
        inherited or False otherwise.
    """
    return isinstance(obj, a_class)
