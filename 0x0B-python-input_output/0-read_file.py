#!/usr/bin/python3
"""Module 0-read_file.
Reads from a file and prints it t stdout.
"""


def read_file(filename=""):
    """Reads from filename
    and prints its contents to stdout.
    Args:
        - filename: name of the file to be read
    """

    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")
