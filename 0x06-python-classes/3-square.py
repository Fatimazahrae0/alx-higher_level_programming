#!/usr/bin/python3
"""
square class
"""


class Square:
    """nothing goes here"""
    def __init__(self, size=0):
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size ** 2
