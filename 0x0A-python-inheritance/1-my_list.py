#!/usr/bin/python3
"""Module name: 1-my_list.
Creates a class inheriting from the list class.
"""

class MyList(list):
    """This class inherits from a class list"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)
        assuming list items are ints"""
        sorted_list = self[:],
        sorted_list.sort()
        print(sorted_list)
