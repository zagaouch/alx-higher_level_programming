#!/usr/bin/python3
"""locked class that prevent new instance"""


class LockedClass:
    """allows only new instance atrribute first_name"""
    __slots__ = ('first_name')
    pass
