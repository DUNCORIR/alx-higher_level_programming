#!/usr/bin/python3
"""
Function checks  if the object is an instance of
a class that inherited from the specified class.
"""


def inherits_from(obj, a_class):
    """Function that returns True if the object is an instance
    of a class that inherited (directly or indirectly) from the
    specified class ; otherwise False.
    

    Args:
        The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if instance of class otherwise False.
    """
    if isinstance(obj, a_class):
        return type(obj) is not a_class
    return False
