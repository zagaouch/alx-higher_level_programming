#!/usr/bin/python3
"""
adds two integer
and returns an integer

"""
def add_integer(a, b=98):
    """
    argument must be an int else raise a type error
    """    
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    a = int(a)
    
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    b = int(b)
    
    result = a + b
    return result
