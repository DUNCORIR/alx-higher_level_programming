#!/usr/bin/python3
import sys

if __name__ == "__main__":

    sum = 0  # initilize sum

    # Loop through the arguments starting from index 1
    for arg in sys.argv[1:]:
        sum = sum + int(arg)  # Convert argument to int and add to total_sum

    # Print the total sum
    print("{}".format(sum))
