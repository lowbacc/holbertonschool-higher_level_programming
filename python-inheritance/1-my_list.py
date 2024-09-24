#!/usr/bin/python3
"""A class MyList which inherits the list"""

class MyList(list):
    """A subclass of the built-in list class."""

    def print_sorted(self):
        """Prints the list elements in ascending order without
        modifying the original list."""
        print(sorted(self))
