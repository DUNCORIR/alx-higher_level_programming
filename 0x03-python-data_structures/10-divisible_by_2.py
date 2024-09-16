#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # initialize empty list
    result_list = []
    # loop thro' each element in input list
    for element in my_list:
        # check if divisible by 2
        if element % 2 == 0:
            # if div by 2,append True to result_list
            result_list.append(True)
        else:
            # append False
            result_list.append(False)
    # Return result list containing True/false values
    return result_list
