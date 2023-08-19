#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    digit = []
    dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    roman = roman_string.upper()
    for string in roman_string:
        if string in dictionary.keys():
            digit.append(dictionary[string])
        else:
            num = 0
            break
    num = 0
    string_length = len(digit)
    for value in range(string_length):
        if value < string_length - 1 and digit[value] < digit[value+1]:
            num = num - digit[value]
        else:
            num = num + digit[value]
    return num
