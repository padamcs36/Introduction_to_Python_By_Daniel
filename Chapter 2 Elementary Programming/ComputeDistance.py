#distance = (x1-x2)^2 + (y1-y2)^2 ** 0.5

x1, y1 = eval(input("Enter x1 and y1 for point 1: "))
x2, y2 = eval(input("Enter x2 and y2 for point 2: "))

#computing the distance with help of two points.
distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
print("The distance between two point is: ", int(distance * 100)/ 100.0)