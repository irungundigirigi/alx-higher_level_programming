#!/usr/bin/python3

def delete_at(my_list=[], idx=o):
    if 0 <= idx < len(my_list):
        new_list = my_list[:idx] + my_list[idx + 1:]
        return new_list
    return new_list
