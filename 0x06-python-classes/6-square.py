#!/usr/bin/python3
"""My square module"""

class Square:
    """Defines the square"""
    def __init__(self, size=0, position=(0, 0)):
        """Create a Square
        Args:
            size: length of side
            position: coordinates
        """
        self.size = size;
        self.position = position;

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """The property of size as side length
        Raises:
            TypeError: if size != int
            ValueError: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """property of square coordinates
        Raises:
            TypeError: if value != a tuple of 2 integers < 0
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of square
        Args: tuple value
        Raises:
            TypeError: if not tuple or tuple has value < 0
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(1, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Get the area of Square
        Returns: size squared
        """
        return self.__size * self.__size

    def pos_print(self):
        """returns the position in spaces """
        pos = ""
        if self.size == 0:
            return "\n"
        for a in range(self.position[1]):
            pos += "\n"
        for a in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """print the square in position"""
        print(self.pos_print(), end='')
