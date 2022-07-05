#!/usr/bin/python3
"""
A function that appends to the end of a file
"""

def append_write(filename="", text=""):
    """Just  a random string to see whats'up"""
    with open(filename, 'a', encoding="UTF-8") as f:
        for c in text:
            f.write(c)
            count += 1

        return (count)
