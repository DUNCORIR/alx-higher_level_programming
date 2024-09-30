#!/usr/bin/python3
import sys  # Import sys module to handle stderr


def safe_function(fct, *args):
    try:
        # Attempt to call function with the provided arguments
        result = fct(*args)
        return result
    except Exception as e:
        # Print the error message to stderr
        sys.stderr.write(f"Exception: {e}\n")
        return None  # Return None indicating an error occurred
