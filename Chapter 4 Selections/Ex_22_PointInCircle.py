#Point in the circle or not
#A point is in the circle if its distance to (0,0) is less than or equal to 10.
#where 10 is radius of the circle
#d = (x2 - x1 ) ^ 2 + (y2 - y1) ^ 2 ** 0.5

RADIUS = 10
x2, y2 = eval(input("Enter a point  with two coodinates: "))
x1 = y1 = 0
d =  ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

if d <= 10:
    print(f"Point {x2 * 10/ 10.0, y2 * 10/ 10.0} is in the circle")
else:
    print(f"Point {x2 * 10 / 10.0, y2 * 10 / 10.0} is not in the circle")