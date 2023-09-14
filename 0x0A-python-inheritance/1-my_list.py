#!/usr/bin/python3
"""inhertate my list"""


class MyList(list):
    def print_sorted(self):
        """Print the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
