#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    # Check if the list is empty
    if my_list is None or len(my_list) == 0:
        # If the list is empty, we don't do anything and return
        return
    # Iterate through the reversed list and print each integer
    reversed_list = my_list[::-1]
    for number in reversed_list:
        print("{:d}".format(number))
