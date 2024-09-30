#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0  # Initialize count.
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count = count + 1  # increament count.
        except IndexError:  # To catch out of range errors.
            break  # Exit loop if index error occurs.
    print()
    return count
