#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    rm_keys = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            rm_keys.append(key)
    for key in rm_keys:
        del a_dictionary[key]
    return a_dictionary
