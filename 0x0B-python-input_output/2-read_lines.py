#!/usr/bin/python3
""" function that reads n lines of
a text file (UTF8) and prints it to stdout
"""


def read_lines(filename="", nb_lines=0):
    """function"""
    with open(filename, mode="r", encoding="utf-8") as f:
        if nb_lines <= 0 or nb_lines >= len(f.readline()):
            f.seek(0)
            print(f.read())
        else:
            for i in range(nb_lines):
                f.seek(0)
                print(f.readlines()[i], end="")
