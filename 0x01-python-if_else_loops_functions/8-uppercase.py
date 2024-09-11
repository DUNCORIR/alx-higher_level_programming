#!/usr/bin/python3
def uppercase(str):
    result = ''
    for c in str:
        if 97 <= ord(c) <= 122:  # Check if c is a lowercase letter
            result = result + chr(ord(c) - 32)
        else:
            # Keep the character as is
            result = result + c
    print(result)
