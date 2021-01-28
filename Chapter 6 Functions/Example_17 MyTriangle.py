import math
def main():
    a, b, c = eval(input("Enter three side of triangle: "))
    area(a, b, c)

def isValid(side1, side2, side3):
    if side1+side2 > side3 and side1+side3 > side2 and side3+side2 > side1:
        return True

def area(side1, side2, side3):
    if isValid(side1, side2, side3) == True:
        s = (side1 + side2 + side3) / 2
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        print("Area of Triangle is: ",area)
    else:
        print("Input is Invalid.")
main()