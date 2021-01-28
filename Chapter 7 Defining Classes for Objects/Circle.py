import math
class circle:
    def __init__(self, radius = 1):
        self.radius  = radius

    def area(self):
        return self.radius * self.radius * math.pi
    def getPerimeter(self):
        return 2 * self.radius * math.pi
    def setRadius(self, radius):
        self.radius = radius
# def main():
#     radius = eval(input("Enter radius of the circle: "))
#     object = circle(radius)
#     print("Area is: ",format(object.area(), ".2f"), "\nPerimeter is: ", format(object.getPerimeter(), ".2f"))
#
# main()
# class A:
#     def __init__(self,i):
#         self.i = i
#
# def main():
#     # a = A() #missing one positional argument error to fix pass value
#     a = A(9) #corrected
#     print(a.i)
# main()