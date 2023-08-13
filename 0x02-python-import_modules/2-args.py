#!/usr/bin/python3
import sys
if __name__ == '__main__':
    words = sys.argv[1:]
    word = len(words)

    if word == 0:
        print('{} arguments.'.format("0"))
    elif word == 1:
        print('{} argument:'.format(word))
    else:
        print('{} arguments:'.format(word))

    for i in range(word):
        print('{}: {}'.format(i + 1, words[i]))
