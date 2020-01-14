#!/usr/bin/python3
"""function that prints My name is <first name> <last name>
if the type of firts name is not str raises an error
if the type of last name is not str raises an error
"""


def say_my_name(first_name, last_name=""):
    """Function that print My name
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')

    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))
