#!/usr/bin/python3
"""
The module provides a function to serialize an object's
attributes into a dictionary with simple data structure.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an
    object for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary representation of the object's attributes.
    """
    return obj.__dict__
