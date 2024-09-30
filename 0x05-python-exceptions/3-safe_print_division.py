#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b  # Attempt the division
    except ZeroDivisionError:
        result = None  # If division by zero occurs, set result to None
    finally:
        print("Inside result: {}".format(result))  # Always print the result
    return result  # Return the result (or None if error occurred)
