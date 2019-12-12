#!/usr/bin/python3
import hidden_4
import sys
if __name__ == "__main__":
    i = 0
    names = dir(hidden_4)
    idx = len(names)
while i < idx:
    if names[i][0] != '_':
        print(names[i])
    i += 1
