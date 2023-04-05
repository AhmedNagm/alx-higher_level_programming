#!/usr/bin/python3
"""Define a locked class"""


class LockedClass:
    """
    Prevent the user from initiating a new LockedClass 
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]


def __init__(self):
    """Creates new instances of Locked Class."""

    self.first_name = "first_name"
