#Given a directed line from the points p0, p1, p2
#Now our task to check wether the p2 is left side, right side or on the same line
#by using formulla
# (x1 - x0) * (y2 - y0) - (x2 - x0)* (y1 - y0) ==0, > = , < 0

x0 , y0, x1, y1, x2, y2 = eval(input("Enter the coordinates for the three points p0, p1, p2: "))

if (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) > 0:
    print("p2 is on the left side of the line")
elif (x1 - x0) * (y2 - y0) - (x2 - x0)* (y1 - y0) == 0:
    print("p2 is on the same line")
else:
    print("p2 is on the right side of the line.")