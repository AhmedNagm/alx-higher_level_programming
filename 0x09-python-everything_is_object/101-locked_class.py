#!/usr/bin/python3

"""Define a locked class"""


class LockedClass:
    """
    Prevent the user from initiating a new LockedClass 
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]