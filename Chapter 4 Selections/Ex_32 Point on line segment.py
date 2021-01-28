
x0 , y0, x1, y1, x2, y2 = eval(input("Enter the coordinates for the three points p0, p1, p2: "))

if (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) == 0:
    print(f"{x2, y2} is on the line segment from {x0, y0} to {x2, y2}")
else:
    print(f"{x2, y2} is not on the line segment from {x0, y0} to {x2, y2}")