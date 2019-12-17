#!/usr/bin/env python3
def no_c(my_string):
    chars = ['c', 'C']
    my_string = ''.join(i for i in my_string if i not in chars)
    return my_string
