#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        a = len(sentence)
        b = sentence[0]
        return (a, b)
    return (0, None)
