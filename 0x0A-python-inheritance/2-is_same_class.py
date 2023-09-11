#!/usr/bin/python3
""" Checks if obj is an instance of a class"""

def is_same_class(obj, a_class):
    """ Return true if obj is an instance of class
    , otherwise false
    """
    return (type(obj) == a_class)
