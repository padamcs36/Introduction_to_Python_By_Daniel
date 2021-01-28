class Rectangle:
    def __init__(self, width = 1, height = 2):
        self.__width = width
        self.__height = height

    def getArea(self):
        return self.__height * self.__width

    def getPerimeter(self):
        return 2 * (self.__width + self.__height)

    def getWidht(self):
        return self.__width

    def getHeight(self):
        return self.__height