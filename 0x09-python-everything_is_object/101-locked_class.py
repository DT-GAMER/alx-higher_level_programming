#!/usr/bin/python3
"""
Locked Class:
    Attributes can't be dynamically created except 'first_name'
"""


class LockedClass:
    """Locked Class
    """
    __slots__ = ["first_name"]

    def __init__(self):
        """Initializing LockedClass object
        """
        pass
