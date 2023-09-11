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

    def area(self):
        """ returns the rectangle area """
        return self.__width * self.__height

    def __str__(self):
        """ return the print() and str() representation of Rectangle """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string