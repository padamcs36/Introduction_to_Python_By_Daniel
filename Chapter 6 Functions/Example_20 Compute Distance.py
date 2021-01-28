import math
def main():
    x1, y1, x2, y2 = eval(input("Enter x1, y1, x2, y2: "))
    computeDistance(x1, y1, x2, y2)

def computeDistance(x1, y1, x2, y2):

    distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    print("Distance is : ", distance)
main()