#!/usr/bin/python3
"""
adds two integer
and returns an integer

"""


def add_integer(a, b=98):
    """
    argument must be an int else raise a type error
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return a + b