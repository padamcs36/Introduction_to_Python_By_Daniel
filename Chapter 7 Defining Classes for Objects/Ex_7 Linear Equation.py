class LinearEquation:
    def __init__(self,a ,b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def getA(self):
        return self.__a
    def getB(self):
        return self.__b
    def getC(self):
        return self.__c
    def getD(self):
        return self.__d
    def getE(self):
        return self.__e
    def getF(self):
        return self.__f

    def isSolovable(self):
        if self.__a * self.__d - self.__b * self.__c != 0:
            return True
        else:
            return False
    def getX(self):
        X = (self.__e * self.__d - self.__b * self.__f) / \
            (self.__a * self.__d - self.__b * self.__c)
        return X

    def getY(self):
        Y = (self.__a * self.__f - self.__e * self.__c) / \
            (self.__a * self.__d - self.__b * self.__c)
        return Y

def main():
    a,b,c,d,e,f = eval(input("Enter a,b,c,d,e,f :: "))
    linearEq = LinearEquation(a,b,c,d,e,f)

    if linearEq.isSolovable():
        print("X is ",format(linearEq.getX(), ".1f"),
              " and Y is: ",format(linearEq.getY(),".1f"))
    else:
        print("Linear Equation has no Solution.")

main()