#!/usr/bin/python3
"""define  an inherited class-checking function"""


def inherits_from(obj, a_class):
    """True if the object isinstance of class that inherited from """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
