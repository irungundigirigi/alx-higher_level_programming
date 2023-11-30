#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(integer_list):
    """
    Args:
        integer_list (list of int): List of integers to find the peak of
    Returns: 
        int: Peak element of the integer_list, or None if the list is empty
    """
    list_size = len(integer_list)
    mid_interval = list_size
    mid_index = list_size // 2

    if list_size == 0:
        return None

    while True:
        mid_interval = mid_interval // 2
        if (mid_index < list_size - 1 and
                integer_list[mid_index] < integer_list[mid_index + 1]):
            if mid_interval // 2 == 0:
                mid_interval = 2
            mid_index = mid_index + mid_interval // 2
        elif mid_interval > 0 and integer_list[mid_index] < integer_list[mid_index - 1]:
            if mid_interval // 2 == 0:
                mid_interval = 2
            mid_index = mid_index - mid_interval // 2
        else:
            return integer_list[mid_index]

