#!/usr/bin/python3
from sys import argv
length = len(argv)
if length == 1:
    print(0)
elif length > 1:
    total = 0
    for i in range(1, length):
        total += int(argv[i])
    print("{:d}".format(total))
