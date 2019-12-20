#!/usr/bin/python3
def roman_to_int(roman_string):
    a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) is not str or roman_string is None:
        return 0
    else:
        r = 0
        if len(roman_string) < 2:
            r = a[roman_string[0]]
        elif len(roman_string) == 2:
            if a[roman_string[-2]] < a[roman_string[-1]]:
                r = a[roman_string[-1]] - a[roman_string[-2]]
        else:
            st = roman_string
            for i in roman_string:
                r += sum(map(lambda x: a[x] if x == i else 0, a))
            d = range(len(st) - 1, 0, -1)
            f = sum(map(lambda x: a[st[x - 1]] if a[st[x]] > a[st[x - 1]]
                    else 0, d))
            r -= 2 * f
    return r
