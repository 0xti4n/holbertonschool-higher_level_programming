#!/usr/bin/python3
""" function that adds a new attribute
to an object if it’s possible
"""


def add_attribute(self, name, new):
    """adds a new attribute to an object"""
    try:
        self.name = new
    except:
        raise TypeError('can\'t add new attribute')
