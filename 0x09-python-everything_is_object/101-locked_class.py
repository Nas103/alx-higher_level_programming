#!/usr/bin/python3
"""Define a locked class. """

class LokckedClass:
    """
    Prevent the user from instantiating new  lockedClass attributes
    for anything but attributes called 'first_name'.
    """

    _slots_ = ["fisrt_name"]
