#!/usr/bin/python3


class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id is None:
            self.id = self.__nb_objects
            Base.__nb_objects += 1
        else:
            self.id = id