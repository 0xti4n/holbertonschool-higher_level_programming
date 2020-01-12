#!/usr/bin/python3


def text_indentation(text):
    if type(text) is not str:
        raise TypeError('text must be a string')
    temp = 0
    for i in text:
        if temp is 1 and i is ' ':
            continue
        if i == '.' or i == '?' or i == ':':
            print(i, end='')
            print('\n')
            temp = 1
        else:
            print(i, end='')
            temp = 0
    print()
