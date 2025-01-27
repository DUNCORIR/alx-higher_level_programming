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

    def to_json(self):
        """
        Retrieves a dictionary representation of student instance.

        Returns;
            dict: A dictionary containing the instance attributes.
        """
        return self.__dict__
