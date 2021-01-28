#Point in the rectangle or not
#width = 10(Horizontal), height = 5(vertical)
#A point is in the rectangle if its horizontal distance to (0,0)  less than or equal to 10/2.
#A point is in the rectangle if its vertical distance to (0,0)  less than or equal to 5/2.
#d = (x2 - x1 ) ^ 2 + (y2 - y1) ^ 2 ** 0.5

x2, y2 = eval(input("enter a point with two coordinates: "))
x1 = y1 = 0
width = 10
height = 5.0
# d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
horizotal = x2 - x1 ** 0.5 #computing horizontal distance (y2 = 0)
vertical = y2 - y1 ** 0.5 #computing vertical distance (x2 = 0)

if horizotal <= width / x2 and vertical <= height / y2:
    print(f"Point {x2, y2} is in the rectangle")
else:
    print(f"Point {x2, y2} is not in the rectangle")