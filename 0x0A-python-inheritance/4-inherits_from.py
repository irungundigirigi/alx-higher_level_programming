#!/usr/bin/python3
""" checks if object is an instance of class that inherited (directly, indirectly) from the specified class or not"""

def is_kind_of_class(obj, a_class):
    """ returns true if condition is met"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)