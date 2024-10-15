#!/usr/bin/python3
"""
The function that returns the JSON representation.
"""


def to_json_string(my_obj):
    """
    Function returns the JSON representation of an object (string


    Args:
        my_obj: The Python object to be serialized into a JSON string.

    Returns:
        str: The JSON string representation of the object.
    """

    import json
    return json.dumps(my_obj)
