#!/usr/bin/python3
import json
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
"""script that adds all arguments to a
Python list, and then save them to a file
"""

try:
    fil = "add_item.json"
    l = load_from_json_file(fil)
except:
    l = []
finally:
    for i in range(len(argv)):
        if i >= 1:
            l.append(argv[i])
    save_to_json_file(l, fil)
