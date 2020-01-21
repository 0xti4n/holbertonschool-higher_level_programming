#!/usr/bin/python3
import json
"""function that creates an Object
from a “JSON file
”"""


def load_from_json_file(filename):
    """Function"""
    with open(filename, mode="r") as f:
        return json.loads(f.read())
