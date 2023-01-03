#!/usr/bin/python3

class Rectangle:

    """

    Class that defines a rectangle.

    """

    def __init__(self, width=0, height=0):

        """

        Initializes a rectangle with optional width and height.

        """

        self.width = width # set the width attribute

        self.height = height # set the height attribute

    @property

    def width(self):

        """

        Retrieves the width of the rectangle.

        """

        return self.__width # return the width attribute

    @width.setter

    def width(self, value):

        """

        Sets the width of the rectangle.

        """

        if not isinstance(value, int): # check if value is an integer

            raise TypeError("width must be an integer") # if not, raise a TypeError

        if value < 0: # check if value is less than 0

            raise ValueError("width must be >= 0") # if it is, raise a ValueError

        self.__width = value # set the width attribute to value

    @property

    def height(self):

        """

        Retrieves the height of the rectangle.

        """

        return self.__height # return the height attribute

    @height.setter

    def height(self, value):

        """

        Sets the height of the rectangle.

        """

        if not isinstance(value, int): # check if value is an integer

            raise TypeError("height must be an integer") # if not, raise a TypeError

        if value < 0: # check if value is less than 0

            raise ValueError("height must be >= 0") # if it is, raise a ValueError

        self.__height = value # set the height attribute to value

