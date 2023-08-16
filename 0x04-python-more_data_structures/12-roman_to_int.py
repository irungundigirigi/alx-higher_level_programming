#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0

    values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    total = 0
    for char in reversed(roman_string):
        total += values[char] if total < values[char] * 5 else -values[char]
    return(total)
