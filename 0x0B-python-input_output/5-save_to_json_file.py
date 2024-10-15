#!/usr/bin/python3
"""
The module contains a function that writes a Python object
to a text file using its JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (onject): The python object to serialize into JSON.
        filename (str): The name of the file to write JSON representation.
    """
    # Open the file using 'with' statement and write mode 'w'
    with open(filename, 'w') as file:
        # Serialize 'my_obj' into JSON and write to the file
        json.dump(my_obj, file)
