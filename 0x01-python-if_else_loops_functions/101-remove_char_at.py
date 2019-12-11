#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    else:
        firts = str[:n]
        last = str[n+1:]
        return firts + last
