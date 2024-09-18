#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Get the sorted list of dictionary keys
    sorted_keys = sorted(a_dictionary.keys())
    # Iterate over sorted keys
    for key in sorted_keys:
        print(f"{key}: {a_dictionary[key]}")
