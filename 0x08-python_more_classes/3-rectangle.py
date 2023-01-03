#!/usr/bin/python
class Rectangle:

    def __init__(self, width=0, height=0):

        """Initialize a rectangle with optional width and height.

        If no width or height are provided, the default value is 0.

        """

        self.width = width

        self.height = height

    

    @property

    def width(self):

        """Return the width of the rectangle."""

        return self._width

    

    @width.setter

    def width(self, value):

        """Set the width of the rectangle.

        Raise a TypeError if the width is not an integer.

        Raise a ValueError if the width is negative.

        """

        if not isinstance(value, int):

            raise TypeError("width must be an integer")

        if value < 0:

            raise ValueError("width must be >= 0")

        self._width = value

    

    @property

    def height(self):

        """Return the height of the rectangle."""

        return self._height

    

    @height.setter

    def height(self, value):

        """Set the height of the rectangle.

        Raise a TypeError if the height is not an integer.

        Raise a ValueError if the height is negative.

        """

        if not isinstance(value, int):

            raise TypeError("height must be an integer")

        if value < 0:

            raise ValueError("height must be >= 0")

        self._height = value

    

    def area(self):

        """Return the area of the rectangle."""

        return self.width * self.height

    

    def perimeter(self):

        """Return the perimeter of the rectangle.

        If either the width or the height is 0, return 0.

        """

        if self.width == 0 or self.height == 0:

            return 0

        return 2 * (self.width + self.height)

    

    def __str__(self):

        """Return a string representation of the rectangle.

        If either the width or the height is 0, return an empty string.

        """

        if self.width == 0 or self.height == 0:

            return ""

        return "\n".join("#" * self.width for _ in range(self.height))



