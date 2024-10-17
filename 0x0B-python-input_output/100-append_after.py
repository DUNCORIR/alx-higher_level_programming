#!/usr/bin/python3
"""
Function that inserts a line of text to a file
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts new line of text to file after each line
    containing a specific string.


    Args;
    filename (str): The name of the file.
    search_string (str): The string to search for in each line.
    new_string (str): The string to insert after each matching line.
    """
    #  Read all lines from file.
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []

    # Iterate through each line.
    for line in lines:
        new_lines.append(line)
        if search_string in line:
            new_lines.append(new_string)

    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)
