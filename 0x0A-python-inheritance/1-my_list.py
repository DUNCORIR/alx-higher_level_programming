#!/usr/bin/python3
"""
The module defines a class Mylist that inherits from list
and includes a method to print list in ascending order.
"""


class MyList(list):
    """A subclass of built in list with additional method to
    print the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints list in ascending order while not
        changing the original.
        """
        print(sorted(self))
