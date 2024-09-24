#!/usr/bin/python3
"""defines object lookup function --> list"""


def lookup(obj):
    """Return list available attributes + methods of object"""
    return dir(obj)
