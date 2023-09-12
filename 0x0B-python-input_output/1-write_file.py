#!/usr/bin/python3
""" Module defines a fn to write to file"""

def write_file(filename="", text=""):
    """ write text to file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

