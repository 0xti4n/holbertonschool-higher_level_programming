#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    ln = len(argv)
    res = 0
    if ln > 1:
        for i in range(1, ln):
            res += int(argv[i])
        print('{:d}'.format(res))
    else:
        print('0')
