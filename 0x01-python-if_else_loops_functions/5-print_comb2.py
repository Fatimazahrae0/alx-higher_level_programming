#!/usr/bin/python3
separator = ", "

for i in range(100):
    if i < 99:
        separator = ", "
    else:
        separator = "\n"

    print("{:02d}{}".format(i, separator), end="")
