#!/usr/bin/python3
"""Add arguments to a list and save them to a file"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'

try:
    item = load_from_json_file(filename)
except Exception:
    item = []

item.extend(sys.argv[1:])
save_to_json_file(item, filename)
