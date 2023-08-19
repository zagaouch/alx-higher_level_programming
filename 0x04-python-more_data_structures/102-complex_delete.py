#!/usr/bin/python3

def complex_delete(my_dictionary, value):
    del_key = []
    for key in my_dictionary:
        if my_dictionary[key] == value:
            del_key.append(key)
    for key in del_key:
        del my_dictionary[key]

    return my_dictionary
