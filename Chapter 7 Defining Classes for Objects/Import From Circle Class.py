from Circle import circle

def main():
    obj = circle()
    n = 5
    printArea(obj, n)
    print("\nRadius is", obj.radius)
    print("n is ", n)
    # print("Perimeter is ", obj.getPerimeter())

def printArea(c, times):
    print("Radius \t\t Area")
    while times >= 1:
        print(c.radius,"\t\t\t", format(c.area(), ".2f"))
        c.radius = c.radius + 1
        times -= 1
        
main()
