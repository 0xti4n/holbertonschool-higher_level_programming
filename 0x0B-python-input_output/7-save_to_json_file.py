#!/usr/bin/python3
import json
"""function that writes an Object to a
text file, using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """Function"""
    with open(filename, mode="w") as f:
        l = json.dumps(my_obj)
        f.write(l)
