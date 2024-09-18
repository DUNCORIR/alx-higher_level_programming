#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_elements = set()
    for elements in set_1:
        if elements in set_2:
            new_elements.add(elements)
    return new_elements
