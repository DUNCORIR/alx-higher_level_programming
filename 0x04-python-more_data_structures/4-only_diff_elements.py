#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_elements = set()
    diff_elements = diff_elements.union(set_2)
    for elements in set_1:
        if elements not in set_2:
            diff_elements.add(elements)
        else:
            diff_elements.remove(elements)
    return diff_elements 
