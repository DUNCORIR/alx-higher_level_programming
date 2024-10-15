#!/usr/bin/python3
"""
Function that appends a string at the end of a text file (UTF8)
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text
    file (UTF8) and returns the number of characters.


    Args:
        Filname (str) : The string to be appended to.
        text (str) : The string to be appended to the file.

    Returns:
        int : The number of characters appended.
    """

    with open(filename, 'a', encoding='utf-8') as file:
        num_characters_appended = file.write(text)  # append text.
    return num_characters_appended  # Return number appended
