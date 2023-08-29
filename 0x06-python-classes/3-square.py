#!/usr/bin/python3
""" A module that defines a square """

class Square:
    """ A class that represemts a square"""
    def __init__(self, size=0):
        """ Initialiazing sqaure
        Args:
            size: size of square defined
        Raises:
            TypeError: if size is not int
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Calculate area
        Returns: The square of the size
        """
        return (self.__size ** 2)
