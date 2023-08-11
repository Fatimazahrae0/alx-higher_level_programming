#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    args = sys.argv[1:]

    print("{} argument{}:".format(num_args, 's' if num_args != 1 else ''))
    
    if num_args == 0:
        print(".")
    else:
        for i, arg in enumerate(args, start=1):
            print("{}: {}".format(i, arg))
