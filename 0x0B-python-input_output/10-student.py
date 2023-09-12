#!/usr/bin/python3
""" Definr class Student"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Instantiate a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the class
        """
        if (type(attrs) == list and
                all(type(elements) == str for elements in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
