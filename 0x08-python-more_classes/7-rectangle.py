#!/usr/bin/python3
"""
module contains a class rectangle that defines a rectangle
"""


class Rectangle:
    """
   defines an a class rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initializes private instance width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrive the private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value for width,with typeerro and valueerror"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrives the private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value for width,with typeerro and valueerror"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """retrives the private instance area"""
        return self.__width * self.__height

    def perimeter(self):
        """retrives the private instance perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """print rectangle shape"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_str = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    if j == self.__width - 1:
                        rectangle_str += Rectangle.print_symbol
                    else:
                        rectangle_str += Rectangle.print_symbol
                if i != self.__height - 1:
                    rectangle_str += "\n"
            return rectangle_str

    def __repr__(self):
        """Return a string of an object of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """delet object of the rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
