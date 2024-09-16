#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # check index is '-' or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list

    # create new list less element at given index
    new_list = my_list[:idx] + my_list[idx + 1:]

    # return modified list
    return new_list
