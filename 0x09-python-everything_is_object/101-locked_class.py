#!/usr/bin/python3
"""Define a locked class"""


class LockedClass:
    __slots__ = ["first_name"]

    def __init__(self):
        pass

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError(
                f"{name} is not an allowed attribute for this class")
        super().__setattr__(name, value)
