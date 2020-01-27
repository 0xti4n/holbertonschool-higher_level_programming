#!/usr/bin/python3
"""class base"""


import json


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file """
        if list_objs is not None:
            l = []
            for i in list_objs:
                name = i.__class__.__name__
                l.append(i.to_dictionary())
                name += ".json"
            with open(name, mode="w") as f:
                f.write(cls.to_json_string(l))
        else:
            name2 = cls.__name__
            name2 += ".json"
            with open(name2, mode="w") as f:
                f.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """from json"""
        if json_string is not None:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """ create"""
        dummy = cls(2, 4, 45, 46)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load from file"""
        try:
            name = cls.__name__
            name += ".json"
            with open(name, mode="r") as f:
                data = cls.from_json_string(f.read())
                l = []
            for i in data:
                l.append(cls.create(**i))
            return l
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to file csv"""
        if list_objs is not None:
            l = []
            for i in list_objs:
                name = i.__class__.__name__
                l.append(i.to_dictionary())
                name += ".csv"
            with open(name, mode="w", newline='') as f:
                f.write(cls.to_json_string(l))

        else:
            name2 = cls.__name__
            name2 += ".csv"
            with open(name2, mode="w") as f:
                f.write("[]")

    @classmethod
    def load_from_file_csv(cls):
        """load from file"""
        name = cls.__name__
        name += ".csv"
        with open(name, mode="r") as f:
            data = cls.from_json_string(f.read())
            l = []
            for i in data:
                l.append(cls.create(**i))
            return l

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw"""
        pass
