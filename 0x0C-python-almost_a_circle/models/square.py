#!/usr/bin/python3
"""Class square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialise the square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set size of square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square"""
        if args:
            for a, arg in enumerate(args):
                if a == 0:
                    self.id = arg
                if a == 1:
                    self.width = arg
                if a == 2:
                    self.height = arg
                if a == 3:
                    self.x = arg
                if a == 4:
                    self.y = arg

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Dictionary Representation of Square class """
        dict = {}
        dict["id"] = self.id
        dict["height"] = self.height
        dict["width"] = self.width
        dict["x"] = self.x
        dict["y"] = self.y
        return dict

    def __str__(self):
        """Displays the rectangle details"""
        return "[Square] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                    self.width, self.height)
