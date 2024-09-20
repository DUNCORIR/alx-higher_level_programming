#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    # Initialize variables
    total_weighted_sum = 0
    total_weight = 0

    # Loop through score
    for score, weight in my_list:
        # update total weighted sum and total weight
        total_weighted_sum += score * weight
        total_weight += weight
    # if total weight is 0 to avoid division by zero
    if total_weight == 0:
        return 0

    # return the weighted average
    return total_weighted_sum / total_weight
