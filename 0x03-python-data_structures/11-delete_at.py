#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # check index is '-' or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Remove element at given index
    del my_list[idx]

    # return modified list
    return my_list
