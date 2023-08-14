#!/usr/bin/python3
def element_at(my_list, idx):
    if 0 > idx:
        return None
    elif idx >= len(my_list):
        return None
    return my_list[idx]
