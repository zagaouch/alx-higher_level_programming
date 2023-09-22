#!/usr/bin/python3
""" An empty class base"""


import json


class Base:
    """defines a class base that has a private attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """static method returns the string [] or JSON string """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
