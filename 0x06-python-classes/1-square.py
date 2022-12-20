#!/usr/bin/python3

"""Define a Square class"""


class Square:
    """ Model a Square
        This class models a typical square
    """

    def __init__(self, size):
        """Initialise a new square object with a size
        Args:
            size (int): the size of the square
        """
        self.__size = size
