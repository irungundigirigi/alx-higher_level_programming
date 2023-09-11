#!/usr/bin/python3
""" inherit from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ a class to define rectangle """
    def __init__(self, width, height):
        """ initialize new rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
