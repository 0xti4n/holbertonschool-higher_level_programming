#!/usr/bin/python3
def uppercase(str):
    for a in str:
        c = ord(a)
        if ord(a) >= 97 and ord(a) <= 122:
            c = ord(a)-32
        print('{:c}'.format(c), end='')
    print()
