#!/usr/bin/python3
"""function that prints a text with 2 new lines
after each of these characters: ., ? and :
if type of text is not str raises an error
"""


def text_indentation(text):
    """function that prints a text with 2 new lines
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    if len(text) != 0:
        text = text.strip()
        temp = 0
        for i in text:
            if temp is 1 and i is ' ':
                temp = 0
                continue
            if i == '.' or i == '?' or i == ':':
                print(i, end='')
                print('\n')
                temp = 1
            else:
                print(i, end='')
                temp = 0
        print()
    else:
        raise TypeError('text must be a string')
