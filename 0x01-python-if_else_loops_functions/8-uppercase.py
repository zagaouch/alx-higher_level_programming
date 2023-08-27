#!/usr/bin/python3
def uppercase(str):
    for c in str:
        x = ord(c)
        if x >= 97 and x <= 122:
            x -= 32
            c = chr(x)
        print('{}'.format(c), end="")
    print()
