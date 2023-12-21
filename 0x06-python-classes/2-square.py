#!/usr/bin/python3

"""Defines a class Square."""

class Square:
    """This class defines a square."""

    def __init__(self, size=0):
        """Initializes a new square.

        Args:
        size (int, optional):Size of the square. Default is 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
