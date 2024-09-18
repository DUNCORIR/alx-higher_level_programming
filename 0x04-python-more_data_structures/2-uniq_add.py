#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = []
    for num in my_list:
        if num not in unique_list:  # Check not already in unique_list.
            unique_list.append(num)  # append to unique_list.
    return sum(unique_list)  # return sum of all unique numbers.
