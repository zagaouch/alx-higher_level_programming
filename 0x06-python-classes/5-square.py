#!/usr/bin/python3
"""class square"""


class Square:
    """Private instance attribute: size"""

    def __init__(self, size=0):

        if type(size) is int:
            pass
        else:
            raise TypeError("size must be an integer")
        if size >= 0:
            self.__size = size
        else:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size ** 2)

    def my_print(self):

        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                print("#" * self.__size)
