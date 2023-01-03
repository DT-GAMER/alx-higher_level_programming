#!/usr/bin/python3
class Rectangle:
    """
    Defines a rectangle with a width and height, and provides methods to calculate
    its area and perimeter.
    """
    # Class attribute to keep track of the number of rectangle instances
    number_of_instances = 0
    
    # Class attribute to store the symbol used for string representation of rectangles
    print_symbol = "#"
    
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with the given width and height.
        If no width or height is provided, the default value is 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    
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
        Raises a TypeError if the value is not an integer.
        Raises a ValueError if the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
        Raises a TypeError if the value is not an integer.
        Raises a ValueError if the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        If the width or height is 0, the perimeter is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
    
    def __str__(self):
        """
        Returns a string representation of the rectangle using the print_symbol attribute.
        If the width or height is 0, returns an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)
        row = symbol * self.width
        return "\n".join([row] * self.height)
    
    def __repr__(self):
        """
        Returns a string representation of the rectangle that can be used to recreate an
        equivalent rectangle using eval().
        """
        return f"Rectangle({self.width}, {self.height})"
    
    def __del__(self):
        """
        Prints a message when the rectangle
