#Right angle triangle palced at (0, 0) and other two points is:
#(200, 0) horizontal (x1, 0)
#(0, 100) vertical (0, y2)
horizotal = 200
vertical = 100
x1 = y1 = 0 #placed at origin
x, y = eval(input("Enter point's x and y coordinates: "))
dHorizontal = (x - x1)  ** 0.5
dVertical = (y - y1) ** 2 ** 0.5 #25.5
if dHorizontal <= horizotal and dVertical <= vertical:
    print("The point is in the triangle")
else:
    print("The point is not in the triangle")
