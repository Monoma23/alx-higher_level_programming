#!/usr/bin/python3
"""Rectangle class"""


class MyInt(int):
    """advanced taskk"""
    def __eq__(self, other):
        """inverted =="""
        return not super().__eq__(other)

    def __ne__(self, other):
        """inverted !="""
        return not super().__ne__(other)
