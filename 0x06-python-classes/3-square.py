#!/usr/bin/python3

"""Define a Square class"""


class Square:
    """ Model a Square
        This class models a typical square
    """

    def __init__(self, size=0):
        """Initialise a new square object with a size
        Args:
            size (int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Compute area of a square
        This is a public instance method that computes the area
        of a square. This method can be accessed by anyone
        """
        return self.__size * self.__size
