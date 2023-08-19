#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    res = []

    for letter in set_1:
        if letter not in set_2:
            res.append(letter)

    for letter in set_2:
        if letter not in set_1:
            res.append(letter)

    return res
