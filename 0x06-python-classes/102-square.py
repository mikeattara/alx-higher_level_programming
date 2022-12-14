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

    @property
    def size(self):
        """Get the size
        This method retrieves the size of a square object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of object
        This method sets the size of the square object.
        Args:
            value (int): the new value to set the size of the object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __eq__(self, other):
        """Equivalent comparison
        This method defines the == comparision of two Squares
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equivalent comparison
        This methid defines the != comparison of two Squares
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparison
        This method defines the < comparison of two Squares
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to comparison
        This method defines the <= comparison of two Squares
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparison
        This method defines the > comparison of two Squares
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to comparison
        This method defines the >= compmarison of two Squares
        """
        return self.area() >= other.area()
