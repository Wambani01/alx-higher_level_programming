#!/usr/bin/python3
"""writes jason representation to a file"""
import json


def save_to_json_file(my_obj, filename):
    """saves python object to json file"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
