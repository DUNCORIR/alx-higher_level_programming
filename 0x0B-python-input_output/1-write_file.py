#!/usr/bin/python3
"""
The function that writes a string to a textfile UTD-8
"""


def write_file(filename="", text=""):
    """
    The function that writes a string to a text file (UTF8)
    and returns the number of characters written.

    Args:
        filename (Str): The string to be written to file.
        text(str): file to be written .

    Returns:
        int: The number of characters written.
    """

    with open(filename, 'w', encoding='utf-8') as file:
        num_characters_written = file.write(text)  # Write text to file
    return num_characters_written  # Return number of charcters.
