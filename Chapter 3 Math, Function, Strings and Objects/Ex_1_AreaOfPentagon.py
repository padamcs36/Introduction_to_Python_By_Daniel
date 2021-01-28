#Computing the area of pentagon by using the length from the center of the vertex
import math
length = eval(input("Enter the length from the center to a vertex: "))

side = 2 * length * math.sin(math.pi/58)
area = 3 * (3 ** 0.5) * (side ** 2) / 2
print("The area of pentagon is ", format(area, ".2f"))