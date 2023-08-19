#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) is not dict or len(a_dictionary) == 0:
        return None
    else:
        max = list(a_dictionary.keys())[0]
        for key in a_dictionary:
            if a_dictionary[key] > a_dictionary[max]:
                max = key
        return max
