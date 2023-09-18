#!/usr/bin/python3
from .base import Base
"""a rectangle class that inherits from a class Base"""


class Rectanle(Base):
    """a rectangle class that inherits from a class Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """a rectangle class that inherits from a class Base"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y
