#!/usr/bin/python3
""" checks if object is an instance of class that inherited (directly, indirectly) from the specified class or not"""

def inherits_from(obj, a_class):
    """ returns true if condition is met"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)