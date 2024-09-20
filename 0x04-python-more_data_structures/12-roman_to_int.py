#!/usr/bin/python3
def roman_to_int(roman_string):
    #  Check if input is a valid string
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    # Dictionary for roman numerals to int values.
    roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
    }
    total = 0  # Initialize total to store final integer value
    prev_value = 0  # Stores value of previous roman numeral.

    # Iterate over Roman numeral string in reverse order
    for character in reversed(roman_string):
        # Get the current Roman numeral value
        current_value = roman_values.get(character, 0)

        if current_value < prev_value:
            # If current value is less than previous, subtract it
            total -= current_value
        else:
            total += current_value
        # Update previous value for next iteration
        prev_value = current_value
    return total
