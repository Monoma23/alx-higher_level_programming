#!/usr/bin/python3
"""yo squaress"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this is Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """str THE user representation of square"""
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.size)

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, value):
        """set w and h with the same value which is value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes using *args and keyword args"""
        if (args):
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                elif i == 1:
                    self.size = v
                elif i == 2:
                    self.x = v
                elif i == 3:
                    self.y = v
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """return dictionary representation of square"""
        mon_dictnr = {}
        mon_dictnr["id"] = self.id
        mon_dictnr["size"] = self.size
        mon_dictnr["x"] = self.x
        mon_dictnr["y"] = self.y
        return mon_dictnr
