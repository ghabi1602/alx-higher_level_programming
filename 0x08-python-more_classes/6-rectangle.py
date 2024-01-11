#!/usr/bin/python3


class Rectangle:
    number_of_instances = 0
    """initialize a rectangle with init special method"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    """define a width getter"""
    @property
    def width(self):
        return self.__width

    """define a width setter"""
    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("width must be >= 0")
        elif type(value) != int:
            raise TypeError("width must be an integer")
        self.__width = value

    """define a height getter"""
    @property
    def height(self):
        return self.__height

    """define a height setter"""
    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height must be >= 0")
        elif type(value) != int:
            raise TypeError("height must be an integer")
        self.__height = value

    """calculate the rectangle area"""
    def area(self):
        return self.__height * self.__width

    """calculate the rectangle perimeter"""
    def perimeter(self):
        if (self.__height == 0) or (self.__width == 0):
            return 0
        return 2 * (self.__height + self.__width)

    """define the __str__ method that prints the rectangle to stdout"""
    def __str__(self):
        if (self.__width == 0) or (self.__height == 0):
            return ""
        rec = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec = rec + "#"
            rec = rec + "\n"
        return rec

    """define the __repr__ method that prints a string repr of the rect"""
    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    """define the del special method"""
    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
