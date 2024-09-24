#!/usr/bin/python3
"""
defines a function that looks if the object is an instance of the class
directly or indirectly
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of,
    or if the object is an instance of a class
    that inherited from, the specified class (directly or indirectly);
    otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if obj is an instance or inherited instance of a_class,
        False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
