#!/usr/bin/python3

"""Defines a class Student"""


class Student:
    """Represents a class"""
    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first name, last name, age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of a Student instance"""
        json_dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": age
        }
        return json_dict
