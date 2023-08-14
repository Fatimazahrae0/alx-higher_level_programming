#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    big_n = my_list[0]
    for i  in my_list:
        if i > big_n:
            big_n = i
    return big_n
