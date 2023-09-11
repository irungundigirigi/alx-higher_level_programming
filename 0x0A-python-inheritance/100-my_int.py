#!/usr/bin/python3
class MyInt(int):
    """
    A custom integer class that inverts the behavior of the == and != operators.

    Args:
        value (int): The integer value to initialize the MyInt object with.

    Attributes:
        value (int): The integer value stored in the MyInt object.
    """

    def __init__(self, value):
        """
        Initialize a MyInt object with the given integer value.

        Args:
            value (int): The integer value to initialize the MyInt object with.
        """
        super().__init__()
        self.value = value

    def __eq__(self, other):
        """
        Compare the MyInt object with another value using the == operator.

        Args:
            other: The value to compare with the MyInt object.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return self.value != other

    def __ne__(self, other):
        """
        Compare the MyInt object with another value using the != operator.

        Args:
            other: The value to compare with the MyInt object.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return self.value == other
