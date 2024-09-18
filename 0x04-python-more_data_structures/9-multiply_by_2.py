#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for key, value in a_dictionary.items():
        # multiply the value by 2
        new_value = value * 2
        # add the key and new value to the new dictionary
        new_dict[key] = new_value
    return new_dict
