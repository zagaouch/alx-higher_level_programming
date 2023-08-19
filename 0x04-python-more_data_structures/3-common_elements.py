#!/usr/bin/python3

def common_elements(set_1, set_2):
    res = []
    for letter in set_1:
        if letter in set_2:
            res.append(letter)

    return res
