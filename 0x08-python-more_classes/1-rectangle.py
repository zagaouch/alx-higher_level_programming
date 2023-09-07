#!/usr/bin/python3$
""" An class rectangle"""
class Rectangle:
    """ define an class"""
    def __init__(self, width=0, height=0):
        """ define an constructor"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ define a property"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value for width,with typeerro and valueerror"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ define a property"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value for height,with typeerro and valueerror"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
