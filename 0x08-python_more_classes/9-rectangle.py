#!/usr/bin/python3
class Rectangle:

    """Class representing a rectangle.

    Attributes:

        number_of_instances: Class attribute representing the number of

            rectangles that have been instantiated.

        print_symbol: Class attribute representing the symbol to use when

            printing a string representation of the rectangle.

    """

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):

        """Initialize a new rectangle with the given width and height.

        Args:

            width: The width of the rectangle.

            height: The height of the rectangle.

        """

        self.width = width

        self.height = height

        Rectangle.number_of_instances += 1

    def __del__(self):

        """Delete a rectangle and print a message."""

        Rectangle.number_of_instances -= 1

        print("Bye rectangle...")

    def __str__(self):

        """Return a string representation of the rectangle.

        If either the width or height is 0, return an empty string.

        """

        if self.width == 0 or self.height == 0:

            return ""

        return "\n".join(self.print_symbol * self.width for _ in range(self.height))

    def __repr__(self):

        """Return a string representation of the rectangle that can be used to

        recreate a new instance using eval().

        """

        return f"Rectangle({self.width}, {self.height})"

    @property

    def width(self):

        """Return the width of the rectangle."""

        return self.__width

    @width.setter

    def width(self, value):

        """Set the width of the rectangle.

        Args:

            value: The new width of the rectangle.

        Raises:

            TypeError: If the width is not an integer.

            ValueError: If the width is less than 0.

        """

        if not isinstance(value, int):

            raise TypeError("width must be an integer")

        if value < 0:

            raise ValueError("width must be >= 0")

        self.__width = value

    @property

    def height(self):

        """Return the height of the rectangle."""

        return self.__height

    @height.setter

    def height(self, value):

        """Set the height of the rectangle.

        Args:

            value: The new height of the rectangle.

        Raises:

            TypeError: If the height is not an integer.

            ValueError: If the height is less than 0.

        """

        if not isinstance(value, int):

            raise TypeError("height must be an integer")

        if value < 0:

            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):

        """Return the area of the rectangle."""

        return self.width * self.height

    def perimeter(self):

        """Return the perimeter of the rectangle.

        If either the width or height is 0, return 0.

        """

        if self.width == 0 or self.height == 0

