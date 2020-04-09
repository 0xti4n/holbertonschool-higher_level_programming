#!/usr/bin/python3
"""Find a peak"""


def find_peak(list_of_integers):
    """Function that find a peak"""
    ls = list_of_integers
    for i in range(1, len(list_of_integers) - 1):
        if ls[i] >= ls[i - 1] and ls[i] >= ls[i + 1]:
            return list_of_integers[i]
