#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_list = []  # create list to hold keys to be deleted
    for key, val in a_dictionary.items():  # Iterate over key value
        if val == value:  # if value matches target value, add key
            delete_list.append(key)

    # Remove the keys in delete_list from the dictionary
    for key in delete_list:
        del a_dictionary[key]

    # Return the modified dictionary
    return a_dictionary
