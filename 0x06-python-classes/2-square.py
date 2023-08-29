#!/usr/bin/python3
"""Defines square"""

class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initialize square
        Args:
            size: size of square
        Raises:
            TypeError: if size is not int
            ValueError: size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
