#!/usr/bin/python3
"""
A script that checks weytng dey sup
"""


def append_write(filename="", text=""):
    """
    Weytin concern me...
    """
    count = 0
    with open(filename, 'a', encoding="UTF-8") as f:
        for c in text:
            f.write(c)
            count += 1

    return (count)
