#!/usr/bin/python3
"""A rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the class
        Args:
            width: Width of rectangle
            height: Height of rectangle
            x: x-coordinate
            y: y-coordinate
            id: Class ID
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.validator("y", value)
        self.__y = value

    def area(self):
        """Returns area of rectangle"""
        return self.__height * self.__width

    def display(self):
        """Displays the rectangle"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Displays the rectangle details"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    @staticmethod
    def validator(attribute, value):
        """Validate setter method
            Args:
                attribute: Attribute name
                value: value
            Raises:
                TypeError if value is not an integer
                ValueError if value is less than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))
