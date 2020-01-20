#!/usr/bin/python3
"""Write a class MyInt that inherits from int"""


class MyInt(int):
    """Function"""
    def __init__(self, value):
        int.__init__(self)
        if type(value) == int:
            self.value = value

    def __eq__(self, val):
        return self.value != val

    def __ne__(self, val):
        return self.value == val
