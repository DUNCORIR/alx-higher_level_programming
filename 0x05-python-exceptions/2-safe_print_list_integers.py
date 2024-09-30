#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):  # Iterate up to x elements
        try:
            # print the element as an integer
            print("{:d}".format(my_list[i]), end="")
            count = count + 1  # Increment the count count += 1
        except (ValueError, TypeError):
            continue  # Ignore non-integer values silently
    print()  # Print a newline after all elements
    return count  # Return the number of integers printed
