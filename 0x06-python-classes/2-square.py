#!/usr/bin/python3
"""define class squar"""


class Square:
    """define object size"""

    def __init__(self, size=0):
        """initialization of object size"""
        if type(size) is int:
            pass

        else:
            raise TypeError("size must be an integer")
        if size >= 0:
            self.__size = size

        else:
            raise ValueError("size must be >= 0")
