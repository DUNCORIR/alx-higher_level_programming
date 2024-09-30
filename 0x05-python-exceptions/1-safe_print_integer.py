#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True  # Value is an integer and printed successfully
    except (ValueError, TypeError):
        return False  # The value is not integer or printing failed.
