#!/usr/bin/python3
for digit1 in range(10):
    # Print each combination with proper formatting
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 0 and digit2 == 1:
            # Special case for the very first combination
            print(f"{digit1:01}{digit2:01}", end="")
        elif digit1 != 9 or digit2 != 9:
            print(f", {digit1:01}{digit2:01}", end="")
print()  # Print a newline at the end
