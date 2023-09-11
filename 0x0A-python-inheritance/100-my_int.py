#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""

class MyInt(int):
    """A custom integer class that inverts the behavior of the == and != operators.

    Args:
        value (int): The integer value to initialize the MyInt object with.

    Attributes:
        value (int): The integer value stored in the MyInt object.
    """

    def __eq__(self, value):
        """Override == operator with !=.

        Args:
            value: The value to compare with the MyInt object.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return self.real != value

    def __ne__(self, value):
        """Override != operator with ==.

        Args:
            value: The value to compare with the MyInt object.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return self.real == value
