#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    con = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            con += 1
        except (TypeError, ValueError):
            pass
    print()
    return con
