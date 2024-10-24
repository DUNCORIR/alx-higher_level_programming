#!/usr/bin/python3
""" The module constains a function that cintains a class base.
"""


import os
import json


class Base:
    """
    Class base for managing id attribute across all classes.
    Attribute:
        __nb_objects: (int): The private class attribute to count objetcts.
    Methods:
        __int__(self, id=None): Initializes base objects with a unique id.
    """
    __nb_objects = 0  # Private class attributes to count number of obects

    def __init__(self, id=None):
        """
        initialize a new instance of Base:
        Args:
            id (int, optional): If provided the instance 's id is set
            otherwise a new id is generated by ++ _nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method that returns the JSON string
        rep of list dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries to convert.

        Returns:
            str: JSON string representation of list dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method that writes the JSON string representation to file.

        Args:
            list_objs (list): A list of instances that inherits from Base.
        """
        filename = cls.__name__ + ".json"
        # If list_objs is None, treat it as an empty list
        list_dicts = (
            [obj.to_dictionary() for obj in list_objs]
            if list_objs else []
        )
        # Converts list of dictionaries to a JSON string
        json_string = cls.to_json_string(list_dicts)
        # Write the JSON string to a file
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Static method that returns list of the JSON string
        representation.

        Args:
            json_string (str): A string representating a list of dictionaries.

        Returns:
            list: The list of dictionaries represented by json string.
        """
        # if json_string is None or empty, return an empty list.
        if json_string is None or json_string == "":
            return []

        # Convert the json string to python list and return it.
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class method that returns an instance
        with all attributes already set.

        Args:
            **dictionary: Dictionary with key_value pairs rep the attributes.

        Returns:
            An instance of the class with updated attributes.
        """
        # Dummy insatnces created using placeholder values.
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Placeholder for width and height
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Placeholder size

        # Updating dummy instance using provided attributes.
        dummy_instance.update(**dictionary)

        # Return fully updated instance
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Class method that returns a list of instances.

        Retuns:
            List: A list of instances of the class.
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []

        with open(filename, "r") as file:
            json_string = file.read()

        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**dict_obj) for dict_obj in list_dicts]
