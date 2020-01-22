#!/usr/bin/python3
"""function that inserts a line of text to a
file, after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Function"""
    with open(filename, mode="r", encoding="utf-8") as f:
        data = f.readlines()
    with open(filename, mode="w", encoding="utf-8") as f:
        for line in data:
            con = 0
            for i in range(len(line)):
                if line[i] == search_string[con]:
                    con += 1
                    if con == len(search_string):
                        line = line + new_string
                        break
                    continue
            f.write(line)
