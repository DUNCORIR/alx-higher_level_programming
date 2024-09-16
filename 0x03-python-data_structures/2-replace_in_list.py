#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:  # Check if the index is negative
        return my_list
    if idx >= len(my_list):  # Check if the index is out of range
        return my_list
    my_list[idx] = element  # If index is valid,rep element at given index
    return my_list
