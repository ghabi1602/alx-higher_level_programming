#!/usr/bin/python3
"""define a Rectangle"""


class Rectangle:
    """initialize a rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    """rectangle width getter"""
    @property
    def width(self):
        return self.__width

    """rectangle width setter"""
    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("width must be >= 0")
        elif type(value) != int:
            raise TypeError("width must be an integer")
        self.__width = value

    """rectangle height getter"""
    @property
    def height(self):
        return self.__height

    """rectangle height setter"""
    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height must be >= 0")
        elif type(value) != int:
            raise TypeError("height must be an integer")
        self.__height = value


