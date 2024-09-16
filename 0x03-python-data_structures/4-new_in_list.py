#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    #  use slicing to create a shallow copy of my_list
    new_list = my_list[:]
    # Check if the index is out of bounds or negative
    if idx < 0 or idx >= len(my_list):
        # if index negative or greater,return copy
        return new_list
    # if index is valid, replace element at point
    new_list[idx] = element
    # return modified list
    return new_list
