#!/usr/bin/python3

def uniq_add(my_list=[]):
    res = []
    sum = 0

    for i in my_list:
        if i not in res:
            sum += i
            res.append(i)

    return sum
