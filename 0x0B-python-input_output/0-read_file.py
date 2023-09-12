#!/usr/bin/python3
""" defines a function that reads a file to stdout """

def read_file(filename=""):
    """ print file contents to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
