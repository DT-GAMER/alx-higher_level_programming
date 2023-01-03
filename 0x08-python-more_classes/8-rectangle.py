#!/usr/bin/python3
class Rectangle:
    """
    A class that represents a rectangle.
    """
    number_of_instances = 0  # Public class attribute to keep track of number of instances

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance with optional width and height.
        """
        self.width = width  # Private instance attribute: width
        self.height = height  # Private instance attribute: height
        Rectangle.number_of_instances += 1  # Increment number of instances

    def __del__(self):
        """
        Print a message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement number of instances

    @property
    def width(self):
        """
        Property to retrieve the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Property setter to set the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Property to retrieve the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Property setter to set the height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the rectangle with the larger area.
        If both rectangles have the same area, return the first one.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def area(self):
        """
        Return the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.
        If the width or height is 0, return 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return a string representation of the rectangle using the print symbol.
        If the width or height is 0, return an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self
