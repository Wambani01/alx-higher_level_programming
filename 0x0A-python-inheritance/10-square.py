#!/urs/bin/python3

"""inherits from Rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defined a square"""
    def __init__(self, size):
        Rectangle.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Rectangle] " + str(self.__size) + "/" + str(self.__size)
