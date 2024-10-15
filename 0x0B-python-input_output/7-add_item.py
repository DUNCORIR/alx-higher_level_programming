#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a file
"""


import sys


# Import the save and load functions from the respective tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    # Try to load the list from the file if it exists
    items = load_from_json_file(filename)
except FileNotFoundError:
    # If the file doesn't exist, start with an empty list
    items = []

# Append all command-line arguments.
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
