#!/usr/bin/python3
"""Defines Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define a square"""
    def __init__(self, size):
        """Initialize new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size