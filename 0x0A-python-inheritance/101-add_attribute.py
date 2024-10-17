#!/usr/bin/python3
"""
Function that adds a new attribute to an object if it’s possible.
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds new attribute to an object if possible.

    Args:
        obj (any): The object to which the attribute will be added.
        attr_name (str): The name of the attribute.
        attr_value (any): The value of the attribute.

    Raises:
        TypeError if the object cannot have new attributes.
    """

    #  Check if the object has __dict__ to allow dynamic attributes.
    if hasattr(obj, "__dict__"):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
