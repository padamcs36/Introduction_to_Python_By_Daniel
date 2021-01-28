import math
print(format("Number", "<10s"), format("Square Root"))
count = 0
while count <= 20:
    print(format(count, "<10d"), format(math.sqrt(count), ".4f"))
    count += 2