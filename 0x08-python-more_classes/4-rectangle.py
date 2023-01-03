#!/usr/bin/python3
class Rectangle:
    """
    Defines a rectangle with private attributes for width and height, and public methods for calculating area and perimeter. The rectangle can be instantiated with optional width and height values, and these values can be set and retrieved using properties. The rectangle can also be printed and represented as a string.
    """
    
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with optional width and height values.
        """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        """
        return self._width
    
    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle to the given value.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value
    
    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        """
        return self._height
    
    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle to the given value.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
    
    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
    
    def __str__(self):
        """
        Returns a string representation of the rectangle using the '#' character.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for _ in range(self.height))
    
    def __repr__(self):
        """
        Returns a string representation of the rectangle that can be used to recreate a new instance using eval().
        """
        return f"Rectangle({self.width}, {self.height})"
