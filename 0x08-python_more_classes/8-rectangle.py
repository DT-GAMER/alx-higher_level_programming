#!/usr/bin/python3
class Rectangle:
    """
    Class that represents a rectangle.
    
    Attributes:
    - width: an integer representing the width of the rectangle.
    - height: an integer representing the height of the rectangle.
    - number_of_instances: a class attribute that keeps track of the number of
      instances of the class.
    - print_symbol: a class attribute that represents the symbol used to print
      the rectangle.
      
    """
    
    # Class attributes
    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the class.
        
        Args:
        - width: an integer representing the width of the rectangle. Default value is 0.
        - height: an integer representing the height of the rectangle. Default value is 0.
        
        """
        # Private instance attributes
        self.__width = width
        self.__height = height
        
        # Increment number of instances
        Rectangle.number_of_instances += 1
        
    # Property for width attribute
    @property
    def width(self):
        """
        Gets the width of the rectangle.
        
        Returns:
        An integer representing the width of the rectangle.
        
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.
        
        Args:
        - value: an integer representing the new width of the rectangle.
        
        Raises:
        - TypeError: if value is not an integer.
        - ValueError: if value is less than 0.
        
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        
    # Property for height attribute
    @property
    def height(self):
        """
        Gets the height of the rectangle.
        
        Returns:
        An integer representing the height of the rectangle.
        
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.
        
        Args:
        - value: an integer representing the new height of the rectangle.
        
        Raises:
        - TypeError: if value is not an integer.
        - ValueError: if value is less than 0.
        
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        
    def area(self):
        """
        Calculates the area of the rectangle.
        
        Returns:
        An integer representing the area of the rectangle.
        
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        
        Returns:
        An integer representing the perimeter of
