#!/usr/bin/python3
"""
The module provides a function `lookup` that returns the list of available
and methods of an object.
"""

def lookup(obj):
    """The function returns the list of available attributes
    and methods of an object.

    Args:
        obj: The object to inspect

    Returns:
        A list of strings representing the name of attributes
        and methods.
    """
    return dir(obj)
