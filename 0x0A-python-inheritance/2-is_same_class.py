#!/usr/bin/python3
"""
The module has function that returns True if the object is exactly
an instance of the specified class; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    checks if object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is exactly an instance otherwise False.
    """
    return type(obj) is a_class
