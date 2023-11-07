#!/usr/bin/python3
"""adds all args to a Python list then save them to file"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


file_name = "add_item.json"
if __name__ == "__main__":
    try:
        maList = load_from_json_file(file_name)
    except FileNotFoundError:
        maList = []
    for w, argmnt in enumerate(sys.argv):
        if w > 0:
            maList.append(argmnt)
    save_to_json_file(maList, file_name)
