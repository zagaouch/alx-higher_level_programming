#!/usr/bin/python3
""" An empty class base"""


class Base:
    """defines a class base that has a private attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            self.id = self.__nb_objects
            Base.__nb_objects += 1
        else:
            self.id = id
