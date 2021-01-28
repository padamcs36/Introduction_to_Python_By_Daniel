def main():
    x0,y0,x1,y1,x2,y2= eval(input("Enter coordinates for the three points p0, p1, and p2: "))
    formulla = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
    if formulla > 0:
        leftOfTheLine()
    elif formulla == 0:
        onTheSameLine()
    else:
        onTheLineSegment()
def leftOfTheLine():
    print("P2 is on the left of the line from p0 to p1.")

def onTheSameLine():
    print("P2 is on the same line from p0 to p1.")

def onTheLineSegment():
    print("P2 is on the Line segment of the line from p0 to p1.")

main()