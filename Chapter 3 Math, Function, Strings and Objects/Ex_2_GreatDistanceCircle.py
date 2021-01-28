#Computing great circle distance
#by using this formulla
# d = radius x arccos(sin(x1) x sin(x2)  + cos(x1) x cos(x2) + cos(y1 - y2)
# radius is radius of earth that is 6371.01km
import math
RADIUS = 6371.01

x1,y1 = eval(input("Enter point 1 (latitude and longitude) in degrees: "))
x2,y2 = eval(input("Enter point 2 (latitude and longitude) in degrees: "))

d = RADIUS * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2))  + math.cos(math.radians(x1)) * math.cos(math.radians(x2)) + math.cos(math.radians(y1) - math.radians(y2)))

print("The distance between two points is ", d, "km")