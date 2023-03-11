#!/usr/bin/python3
if __name__ == '__main__':
    '''print result of addition of arguments'''
    import sys

    result = 0
    n = len(sys.argv)
    for i in range(1, n):
        result += int(sys.argv[i])
    print('{}'.format(result))
