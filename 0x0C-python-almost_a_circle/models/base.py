#!/usr/bin/python3
# base.py
""" Define a base nodel class """
import json
import csv


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Return the JSON serialization of a dictionary.
            *static method - no access to class state

            Args:
                list_dictionaries(list): A list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Write the JSON serialization of class instances to file.
            Args:
                list_objs (list):  A list of inherited Base Instances
        """
        file = cls.__name__+".json"
        with open(file, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                json_file.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Deserialize a JSON string and return the resulting Python list.

        Args:
            json_string (str): A JSON string representation of a list of dictionaries.

        Returns:
            If json_string is None or empty, it returns an empty list.
            Otherwise, it returns the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Returns class instanciated from dict
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
    @classmethod
    def load_from_file(cls):
        """
            Return a list of classes instantiated from a JSON strings from a file
            Read from '<cls.__name__>.json'

            Returns:
                If the file does not exist - an empty list
                Else - a list of instantiated classes
        """
        file = str(cls.__name__) + ".json"
        try:
            with open(file, "r") as jsonfile:
                dict_list = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in dict_list]
        except IOError:
            return []

