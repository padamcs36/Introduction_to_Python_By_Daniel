import math
#summation of the series
sum = 0
for i in range(1, 625 + 1):
    sum += 1 / (math.sqrt(i) + math.sqrt(i+1))
print("Summation is: ",format(sum, ".2f"))