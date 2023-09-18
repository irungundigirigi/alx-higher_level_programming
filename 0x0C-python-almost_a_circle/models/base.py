#!/usr/bin/python3

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

