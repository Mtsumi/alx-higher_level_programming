#!/usr/bin/python3
"""Reads from a file and prints it to stdout."""


def read_file(filename=""):
    """Reads file and prints its contents to stdout."""
    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")
