#!/usr/bin/python3
class Rectangle:
    # Class attribute to keep track of the number of instances
    number_of_instances = 0
    
    def __init__(self, width=0, height=0):
        # Initialize the width and height instance attributes
        self.width = width
        self.height = height
        
        # Increment the number of instances
        Rectangle.number_of_instances += 1
    
    def __del__(self):
        # Decrement the number of instances
        Rectangle.number_of_instances -= 1
        
        # Print message when an instance is deleted
        print("Bye rectangle...")
    
    # Define a property for the width attribute
    @property
    def width(self):
        return self._width
    
    # Define the setter for the width attribute
    @width.setter
    def width(self, value):
        # Check if value is an integer
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        
        # Check if value is greater than or equal to 0
        if value < 0:
            raise ValueError("width must be >= 0")
        
        self._width = value
    
    # Define a property for the height attribute
    @property
    def height(self):
        return self._height
    
    # Define the setter for the height attribute
    @height.setter
    def height(self, value):
        # Check if value is an integer
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        
        # Check if value is greater than or equal to 0
        if value < 0:
            raise ValueError("height must be >= 0")
        
        self._height = value
    
    def area(self):
        # Return the area of the rectangle
        return self.width * self.height
    
    def perimeter(self):
        # Return the perimeter of the rectangle
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
    
    def __str__(self):
        # Return a string representation of the rectangle using '#' characters
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for _ in range(self.height))
    
    def __repr__(self):
        # Return a string representation of the rectangle that can be used to recreate an instance
        return f"Rectangle({self.width}, {self.height})"
