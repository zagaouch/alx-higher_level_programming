#!/usr/bin/python3
""" An empty class base"""


class Base:
    """defines a class base that has a private attribute"""
    __nb_objects = 1

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
