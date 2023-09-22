#!/usr/bin/python3
# base.py
""" Define a base node class """

import json
import csv
import turtle


class Base:
    """
    Base class for node objects.

    Attributes:
        __nb_objects (int): The number of Base instances created.
        id (int): The unique identifier for each instance.

    Methods:
        __init__(self, id=None):
            Initializes a new Base instance with an optional ID.

        to_json_string(list_dictionaries):
            Converts a list of dictionaries to a JSON string representation.

        save_to_file(list_objs):
            Writes a list of class instances to a JSON file.

        from_json_string(json_string):
            Deserializes a JSON string into a Python list of dictionaries.

        create(**dictionary):
            Creates a new instance from a dictionary representation.

        load_from_file():
            Loads instances from a JSON file and returns them as a list.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new Base instance.

        Args:
            id (int): The unique identifier for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON serialization of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON string representation of the list.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON serialization of class instances to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        file = cls.__name__ + ".json"
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
            list: The Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns a class instance instantiated from a dictionary.

        Args:
            dictionary (dict): A dictionary representation of the class instance.

        Returns:
            Base: An instance of the class.
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
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Square shapes using  turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turtle = turtle.Turtle()
        turtle.screen.bgcolor("#b7312c")
        turtle.pensize(3)
        turtle.shape("turtle")

        turtle.color("#ffffff")
        for rectangle in list_rectangles:
            turtle.showturtle()
            turtle.up()
            turtle.goto(rect.x, rect.y)
            turtle.down()
            for i in range(2):
                turtle.forward(rect.width)
                turtle.left(90)
                turtle.forward(rect.height)
                turtle.left(90)
            turtle.hideturtle()

        turtle.color("#b5e3d8")
        for square in list_squares:
            turtle.showturtle()
            turtle.up()
            turtle.goto(sq.x, sq.y)
            turtle.down()
            for i in range(2):
                turtle.forward(sq.width)
                turtle.left(90)
                turtle.forward(sq.height)
                turtle.left(90)
            turtle.hideturtle()

        turtle.exitonclick()
