#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []  # Initialize empty list to store results

    for i in range(list_length):
        try:
            # Try dividing corresponding elements
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0  # If division by zero, set result to 0
        except TypeError:
            print("wrong type")
            result = 0  # If incorrect type, set result to 0
        except IndexError:
            print("out of range")
            result = 0  # If out of range, set result to 0
        finally:
            result_list.append(result)  # Append the result to the list
    return result_list  # Return the final list after the loop
