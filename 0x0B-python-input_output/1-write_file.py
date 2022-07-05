#!/usr/bin/python3

"""
A script that writes to a file and returns the number of characters
"""

def write_file(filename="", text=""):
    """Function that returns the number of character written in a file"""
    count = 0
    with open(filename, mode='w' encoding='UTF+8') as filen:
        for c in text:
            filen.write(c)
            count += 1


    return (count)
