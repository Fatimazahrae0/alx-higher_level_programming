#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    for n in range(0, x):
        try:
            print("{}".format(my_list[n]), end="")
            i = i + 1
        except Exception:
            print("", end="")
    print("")
    return i
