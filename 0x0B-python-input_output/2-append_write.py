#!/usr/bin/python3
""" Module defines a function to append file """

def append_write(filename="", text=""):
    """ Appends a string at end of UTF8 text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

