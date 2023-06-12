#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not type(my_list) is list:
        return
    for i in my_list[::-1]:
        print("{:d}".format(i))
