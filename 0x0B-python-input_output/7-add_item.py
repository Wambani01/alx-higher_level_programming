#!/usr/bin/python3

"""adds items to json file"""
import sys
import json


load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file
my_list = []
my_list = load("add_item.json") 
my_list = my_list.append(sys.argv[1:])
save(my_list, "add_item.json")
