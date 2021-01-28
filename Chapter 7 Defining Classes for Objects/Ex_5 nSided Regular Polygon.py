import math
class RegularPolygon:
    def __init__(self, n = 3, side = 1, x = 0, y = 0):
        self.__side = side
        self.__n = n
        self.__x = x
        self.__y = y

    def getN(self):
        return self.__n
    def getSide(self):
        return self.__side
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y

    def setN(self, n):
        self.__n = n
    def setSide(self, side):
        self.__side = side
    def setX(self, x):
        self.__x = x
    def setY(self, y):
        self.__y = y

    def getPerimeter(self):
        return self.__side * self.__n

    def getArea(self):
        area = self.__n * (self.__side ** 2) / (4 * math.tan(math.pi / self.__n))
        return area

    def displayProperties(self):
        print("Perimeter of the Polygon is ",format(self.getPerimeter(),".3f"),
              "\nArea of the Polygon is ",format(self.getArea(), ".3f"),"\n\n")
def main():
    polygon1 = RegularPolygon()
    polygon1.displayProperties()
    polygon1.setX(50)
    # print(polygon1.getX())


    polygon2 = RegularPolygon(6, 4)
    polygon2.displayProperties()

    polygon3 = RegularPolygon(10, 4, 5.6, 7.8)
    polygon3.displayProperties()

main()