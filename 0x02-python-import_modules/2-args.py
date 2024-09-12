#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg_count = len(sys.argv) - 1  # Subtract 1 to exclude the script name

    # Handling the cases for number of arguments
    if arg_count == 0:
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_count))

    # Loop to print each argument with its index, starting from 1
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
