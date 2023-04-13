#!/usr/bin/python3
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = []
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])

file = "add_item.json"

if not os.path.isfile(file):
    save_to_json_file(my_list, file)
else:
    obj = load_from_json_file(file)
    obj += my_list
    save_to_json_file(obj, file)
