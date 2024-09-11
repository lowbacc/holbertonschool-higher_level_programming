#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0

    for i in range(len(roman_string)):
        curr_val = roman_values[roman_string[i]]
        prev_val = roman_values[roman_string[i - 1]] if i > 0 else 0

        if i > 0 and curr_val > prev_val:
            total += curr_val - 2 * prev_val
        else:
            total += curr_val

    return total
