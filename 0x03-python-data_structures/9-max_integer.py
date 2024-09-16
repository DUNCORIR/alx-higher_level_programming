#!/usr/bin/python3
def max_integer(my_list=[]):
    # check if list is empty
    if len(my_list) == 0:
        return None

    # Assuming first element as largest
    largest = my_list[0]

    # iterate thro' list starting from second element
    for i in range(1, len(my_list)):
        if my_list[i] > largest:
            largest = my_list[i]  # update if current largest

    # return largest element found
    return largest
