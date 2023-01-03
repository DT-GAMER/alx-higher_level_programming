#!/usr/bin/python3
class Rectangle:
    """
    Defines a rectangle by its width and height.

    Attributes:
        width (int): the width of the rectangle.
        height (int): the height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with optional width and height.

        Args:
            width (int): the width of the rectangle. Defaults to 0.
            height (int): the height of the rectangle. Defaults to 0.

        Raises:
            TypeError: if width or height is not an integer.
            ValueError: if width or height is less than 0.
        """
        self.width = width
        self.height = height

    def __repr__(self):
        """
        Returns a string representation of the rectangle.
        """
        return f'Rectangle({self.width}, {self.height})'

    def __str__(self):
        """
        Returns a string representation of the rectangle as a rectangle of # characters.
        """
        if self.width == 0 or self.height == 0:
            return ''
        else:
            return '\n'.join(['#' * self.width] * self.height)

    def __del__(self):
        """
        Prints a message when the rectangle is deleted.
        """
        print('Bye rectangle...')

    @property
    def width(self):
        """
        Returns the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): the new width of the rectangle.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Returns the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): the new height of the rectangle.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
