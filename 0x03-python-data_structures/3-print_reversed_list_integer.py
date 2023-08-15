#!/usr/bin/python3
def reverse_list_integer(my_list=[]):
    new_list = []
    for i in range(len(my_list) - 1, -1, -1):
        new_list.append(my_list[i])
    return new_list
