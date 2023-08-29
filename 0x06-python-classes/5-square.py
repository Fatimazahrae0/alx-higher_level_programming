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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        if self.size == 0:
            print("")
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print("")
