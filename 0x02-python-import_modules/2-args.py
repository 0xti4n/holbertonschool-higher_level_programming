#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    result = len(argv)
    if result > 1:
        if result == 2:
            print('1 argument:')
            print('1: {:s}'.format(argv[1]))
        else:
            print('{:d} arguments:'.format(len(argv) - 1))
            i = 1
            while (i < result):
                print('{:d}: {:s}'.format(i, argv[i]))
                i += 1
    else:
        print('0 arguments.')
