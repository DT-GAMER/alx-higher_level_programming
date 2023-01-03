#!/usr/bin/python3

class Rectangle:

    """

    Defines a rectangle with a private instance attribute width and a private instance attribute height.

    """

    

    def __init__(self, width=0, height=0):

        """

        Initializes the rectangle with optional width and height values.

        """

        self.width = width

        self.height = height

    

    @property

    def width(self):

        """

        Returns the width of the rectangle.

        """

        return self._width

    

    @width.setter

    def width(self, value):

        """

        Sets the width of the rectangle.

        Raises a TypeError if value is not an integer.

        Raises a ValueError if value is less than 0.

        """

        if not isinstance(value, int):

            raise TypeError("width must be an integer")

        if value < 0:

            raise ValueError("width must be >= 0")

        self._width = value

    

    @property

    def height(self):

        """

        Returns the height of the rectangle.

        """

        return self._height

    

    @height.setter

    def height(self, value):

        """

        Sets the height of the rectangle.

        Raises a TypeError if value is not an integer.

        Raises a ValueError if value is less than 0.

        """

        if not isinstance(value, int):

            raise TypeError("height must be an integer")

        if value < 0:

            raise ValueError("height must be >= 0")

        self._height = value

    

    def area(self):

        """

        Returns the area of the rectangle.

        """

        return self.width * self.height

    

    def perimeter(self):

        """

        Returns the perimeter of the rectangle.

        Returns 0 if width or height is equal to 0.

        """

        if self.width == 0 or self.height == 0:

            return 0

        return 2 * (self.width + self.height)




