#!/usr/bin/python3

"""Define a Square class"""


class Square:
    """ Model a Square
        This class models a typical square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialise a new square object with a size
        Args:
            size (int): the size of the square
            position (int, int): the tuple of two positive numbers
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Get the position
        This method gets the position of the square object
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the object
        This method sets the position of the square object
        Args:
            value (tuple): a tuple of 2 positive integers to set the
            position of the square object
        """
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(i, int) for i in value)
                or not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """Print the square value and position of the object
        This method prints the square with the character
        '#' and the position of the object
        """
        if self.__size == 0:
            print("")
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
