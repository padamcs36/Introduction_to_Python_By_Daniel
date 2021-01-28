import math
count = 0
print(format("Degree", "<10s"), format("Sin", "<10s"), format("Cos"))
while count <= 360:
    print(format(count, "<6d"), format(math.sin(math.degrees(count)), "10.4f"), format(math.cos(math.degrees(count)), ".4f"))
    count += 10