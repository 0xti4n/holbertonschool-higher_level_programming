#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    a = 0
    for i in my_list:
        if i % 2 == 0:
            new_list.insert(a, True)
        else:
            new_list.insert(a, False)
        a += 1
    return new_list
