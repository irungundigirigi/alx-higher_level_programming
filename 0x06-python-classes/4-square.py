#!/usr/bin/python3
"""Defines a square"""

class Square:
    """ A class that represents a square"""

    def __init__(self, size=0):
        """initializing this square class
        Args:
            size: square size
        Raises:
            TypeError: if size is not int
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Retrieves size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate square area
        Returns: The square area
        """
        return (self.__size ** 2)
