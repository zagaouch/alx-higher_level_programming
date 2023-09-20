#!/usr/bin/python3
"""creates a function Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """takes in similar arguments to rectangle"/
        "replaces width and height with size"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
            string representation of Square class instance
        """
        return "[{}] ({}) {}/{} - {}" \
            .format(self.__class__.__name__, self.id,
                    self.x, self.y, self.size)
