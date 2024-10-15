#!/usr/bin/python3
"""
The module contains a function that creates a python
object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
     fielname (str): The name of the file containing the
     JSON string.

    Returns:
    Object: the python object resulting from the
    JSON deserialization.
    """
    # Open the file using 'with' statement and read mode 'r'
    with open(filename, 'r') as file:
        # Load the JSON content and convert it into a Python object
        obj = json.load(file)

    # Return the created object
    return obj
