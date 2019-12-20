#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        a = sum(map(lambda x: x[0] * x[1], my_list))
        b = sum(map(lambda x: my_list[x][1], range(len(my_list))))
        return a / b
    return 0
