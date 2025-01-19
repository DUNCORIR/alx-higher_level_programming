#!/usr/bin/python3
""""
This function finds peak in a list of unsorted integers using binary search.
"""


def find_peak(list_of_integers):
    """This function finds a peak element in the list using binary search."""
    if not list_of_integers:
        return None  # Return None if the list is empty.

    def binary_search(arr, low, high):
        """Perform binary search to find the peak element."""
        mid = (low + high) // 2

        # Check if the middle element is a peak.
        if (mid == 0 or arr[mid - 1] <= arr[mid]) and \
           (mid == len(arr) - 1 or arr[mid + 1] <= arr[mid]):
            return arr[mid]

        # If the left neighbor is greater, search the left half.
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            return binary_search(arr, low, mid - 1)

        # Otherwise, search the right half.
        else:
            return binary_search(arr, mid + 1, high)

    return binary_search(list_of_integers, 0, len(list_of_integers) - 1)
