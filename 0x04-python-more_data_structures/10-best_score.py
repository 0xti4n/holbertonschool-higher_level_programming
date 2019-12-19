#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        a = 0
        for k, v in a_dictionary.items():
            if v > a:
                a = v
                c = k
        return c
