#!/usr/bin/python3
"""Function that returns an object"""


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to be deserialized.

    Returns:
        object: The Python data structure
        corresponding to the JSON string.
    """
    import json
    return json.loads(my_str)
