#!/usr/bin/python3
"""Write a class Student that defines a student by"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

    def to_json(self, attrs=None):
        if type(attrs) is list:
            d = {}
            for i in attrs:
                if type(i) is str:
                    try:
                        d[i] = getattr(self, i)
                    except AttributeError:
                        continue
            return d
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
