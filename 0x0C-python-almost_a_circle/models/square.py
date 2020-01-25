#!/usr/bin/python3
"""Class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ('[Square] ({}) {}/{} - {}'.format(self.id, self.x,
                self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            l = ["id", "width", "x", "y"]
            con = 0
            for i in args:
                setattr(self, l[con], i)
                con += 1
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        l = ["id", "size", "x", "y"]
        d = {}
        for i in range(len(l)):
            d[l[i]] = getattr(self, l[i])
        return d
