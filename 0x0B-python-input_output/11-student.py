#!/usr/bin/python3
"""
The module contains class Student that defines a student.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of student instance.

        If attrs is a list of strings, only attributes contained in
        this list are retrieved. Otherwise, all attributes are retrieved.
        """
        if isinstance(attrs, list) and \
                all(isinstance(attr, str) for attr in attrs):
            return {
                attr: self.__dict__[attr]
                for attr in attrs if attr in self.__dict__}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        with values from the json dictionary.

        Args:
            json (dict): A dictionary where keys are the attribute
            names and values are the new values to assign.
        """
        for key, value in json.items():
            setattr(self, key, value)
