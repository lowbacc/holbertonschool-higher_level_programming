#!/usr/bin/python3
"""function that returns True if the object is exactly
an instance of the specified class"""


def is_same_class(obj, a_class):
    """
    Check if obj is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to match.

    Returns:
        True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
