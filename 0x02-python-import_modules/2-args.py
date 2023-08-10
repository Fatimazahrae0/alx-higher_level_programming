#!/usr/bin/python3
if __name__ == "__main__":
    """print the list of element"""
import sys
if len(sys.argv) == 0:
    print("0 arguments.")
else:
    print("{:d} arguments:".format(len(sys.argv) - 1))
for i in range(len(sys.argv) - 1):
    print("{:d} : {:s}".format(i + 1, sys.argv[i + 1]))
