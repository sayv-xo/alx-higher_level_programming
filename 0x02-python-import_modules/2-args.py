#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    '''print number and lists of arguments'''
    args = len(sys.argv) - 1
    if args == 0:
        print('{} arguments.'.format(args))
    elif args == 1:
        print('{} argument:'.format(args))
        print('{}: {}'.format(args, sys.argv[1]))
    else:
        print('{} arguments:'.format(args))
        for i in range(1, args + 1):
            print('{}: {}'.format(i, sys.argv[i]))
