#!/usr/bin/python3
class rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        @property
        def width(self):
            return self._width

        @setter.width
        def width(self, value):
            if not isinstance(value, int):
                TypeError('width must be an integer')
            if value < 0:
                raise ValueError('width must be >= 0')
            self._width

        @property
        def height(self):
            return self._height

        @setter.height
        def height(self, value):
            if not isinstance(value, int):
                TypeError('height must be an integer')
            if value < 0:
                raise ValueError('width must be >= 0')
            self._height = value

        def area(self):
            return self.width * self.height

        def perimeter(self):
            if not self.width or not self.height:
                return 0
            return 2 * (self.width + self.height)
