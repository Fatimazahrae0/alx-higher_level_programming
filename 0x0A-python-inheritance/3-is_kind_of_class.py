#!/usr/bin/python3
""" define the class"""


def is_kind_of_class(obj, a_class):
    """check if the obj is instance or not"""
    if isinstance(obj, a_class):
        return True
    return False
