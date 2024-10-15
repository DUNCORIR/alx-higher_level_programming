#!/usr/bin/python3
"""
The module reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read.Defaults
        to an empty string.
    """
    # Use the with statement to open the file safely.
    with open(filename, 'r', encoding='utf-8') as file:
        # Read the entire content of the file.
        content = file.read()
        # Print the content to stdout
        print(content.strip())
