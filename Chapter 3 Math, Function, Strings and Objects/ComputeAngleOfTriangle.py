import math
x1,y1,x2,y2,x3,y3 = eval(input("Enter 6 coordinates points x1,y1,x2,y2,x3,y3: "))

#computing three side of the triangle
a = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
c = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

#computing three angle of the triangle
A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - a * a - b * b) / (-2 * a * b)))

print("Three angles are", round(A * 100)/100.0,round(B * 100)/100.0, round(C * 100)/100.0)