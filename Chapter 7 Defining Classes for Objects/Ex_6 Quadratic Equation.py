import math
class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getA(self):
        return self.__a
    def getB(self):
        return self.__b
    def getC(self):
        return self.__c

    def getDiscriminant(self):
        return self.__b ** 2 - 4 * self.__a * self.__c

    def getRoot1(self):
        r1 = (- self.__b + math.sqrt(self.__b ** 2 - 4 * self.__a * self.__c)) / (2 * self.__a)
        return r1

    def getRoot2(self):
        r2 = (- self.__b - math.sqrt(self.__b ** 2 - 4 * self.__a * self.__c)) / (2 * self.__a)
        return r2

    def displayProperties(self):
        if self.getDiscriminant() > 0:
            print(f"Equation has two roots",format(self.getRoot1(),".3f")," and ",
                  format(self.getRoot2(),".3f"))
        elif self.getDiscriminant() == 0:
            print(f"Equation has one roots", format(self.getRoot1(),".3f"))
        else:
            print("Equation has no real roots.")
def main():
    roots = QuadraticEquation(1, 3.0, 1)
    roots.displayProperties()

main()