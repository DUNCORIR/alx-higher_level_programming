#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None  # Return None if the dictionary is empty or None

    best_key = None  # This will hold the key with the best score
    best_value = float('-inf')  # initialize best value with -ve inf

    for key, value in a_dictionary.items():
        if value > best_value:
            best_value = value  # If current value greater than  best_value
            best_value = key  # Update best_key to the current key

return best_key  # Return the key with the best score
