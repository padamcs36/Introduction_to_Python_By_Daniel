import math
class circle:
    def __init__(self, radius = 1):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def getArea(self):
        return self.__radius * self.__radius * math.pi

c = circle(5)
# AttributeError: 'circle' object has no attribute '__radius'
# print(c.__radius)
#we cannot access direct radius outside the class.
#with the help of method we can access the radius varaible
print("Radius of Circle : ", c.getRadius())
print("Perimter of Circle : ", c.getPerimeter())

# class A:
#     def __init__(self, i):
#         self.__i = i #cannot be accessible directly
# def main():
#     a = A(5)
#     print(A.__i) #AttributeError: type object 'A' has no attribute '__i'
# main()

