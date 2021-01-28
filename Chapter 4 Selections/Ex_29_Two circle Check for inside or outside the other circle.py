#Check wether the circle1 is inside the circle two or not
#inside circle condition is c2 and c1 distance is less than or equal to |r1 + r2|//2
#overlap circle condition is c2 and c1 distance is less than or equal to |r1 - r2|//2

x1, y1, r1 = eval(input("Enter circle1's x-, y-coordinates, and radius: "))
x2, y2, r2 = eval(input("Enter circle2's x-, y-coordinates, and radius: "))

parentCircle = x1 - x2 if x1 - x2 >= 0 else x2 - x1
childCircle = y1 - y2 if y1 - y2 >= 0 else y2 - y1

if parentCircle <= (r1 - r2)//2 and childCircle <= (r1 - r2)//2:
    print("Circle2 is inside the circle1")
elif parentCircle <= (r1 + r2)// 2 and childCircle <= (r1 + r2)//2:
    print("circle2 overlap circle1")
else:
    print("Circle2 does not overlap circle1")