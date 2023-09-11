#!/usr/bin/python3

class BaseGeometry:
    """ class represents a base geometry """
    def area(self):
        """ Method not implemented yet """
        raise Exception("area() is not defined")

    def integer_validator(self, name, value):
        """ validate a value as an int
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
