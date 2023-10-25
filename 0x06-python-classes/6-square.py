#!/usr/bin/python3
"""Defines a 'Square' class with a private instance attribute."""


class Square:
    """Definition of 'Square'"""
    def __init__(self, size=0, position=(0, 0)):
        """Inits Square with a size integer.

        Args:
            size: An integer size of the square.
            position: A tuple of the position of the square.

        Raises:
            TypeError: Size is not an int or position is not a tuple of ints.
            ValueError: Size is negative.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Gets the size of the square.

            Returns:
                The size attribute of the square.
        """
    return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with a value.

            Args:
                value: value to assign to size.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position of the square.

        Returns:
            Position of the Square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square

        Args:
            value: value to set the position
        """
        errMsg = TypeError("position must be a tuple of 2 positive integers")

        if type(value) is not tuple or len(value) != 2:
            raise errMsg
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise errMsg
        elif value[0] < 0 or value[1] < 0:
            raise errMsg

        self.__position = value

    def area(self):
        """Computes the area of the square."""
        return self.__size ** 2

    def my_print(self):
        printSize = self.__size
        if printSize == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(printSize):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(printSize):
                    print("#", end="")
                print()
