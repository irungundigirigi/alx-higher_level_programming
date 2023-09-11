#!/usr/bin/python3
"""This module defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.

    Args:
        obj: The object to which you want to add an attribute.
        att: The name of the attribute you want to add.
        value: The value you want to assign to the attribute.

    Raises:
        TypeError: If it's not possible to add a new attribute to the object.
    """
    try:
        setattr(obj, att, value)
    except AttributeError:
        raise TypeError("can't add new attribute")
