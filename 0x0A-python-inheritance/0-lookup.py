#!/usr/bin/python3
"""This creates a function with prototype lookup(obj)"""


def lookup(obj):
    """
    return a list of the attributes and methods of an object.
    """
    attributes_and_methods = dir(obj)
    return attributes_and_methods
