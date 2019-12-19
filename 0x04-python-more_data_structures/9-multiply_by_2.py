#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for k, val in new.items():
        new[k] = val * 2
    return new
