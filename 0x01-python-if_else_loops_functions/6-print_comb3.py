#!/usr/bin/python3
for i in range(0, 9):
    for x in range(0, 10):
        if i < x and i != 8:
            print('{}{}'.format(i, x), end=", ")
        if i == 8 and i < x:
            print('{}{}'.format(i, x))

