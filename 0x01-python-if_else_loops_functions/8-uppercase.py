#!/usr/bin/python3
def uppercase(str):
    result = ''
    for c in str:
        if 'a' <= c <= 'z':  # Check if c is a lowercase letter
            result = result + chr(ord(c) - 32)
        else:
            result = result + c  # Accumulate as is
    print("{}".format(result))  # Print result after processing all characters
