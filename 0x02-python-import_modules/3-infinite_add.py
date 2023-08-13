#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    sum = 0
    num = sys.argv[1:]
    num_count = len(num)

    for x in range(num_count):
        sum = sum + int(num[x])
    print(sum)
