import math
import time
#1/3 + 3/5 + 5/7+......+97//99
#2n-1/2n+1

sum = 0
for i in range(1, 100, 2):
    k = i / (i+2)
    sum += k
print(format(sum, ".2f"))

#Compute Value of PI
sum = 0
startTime = time.time()
for i in range(1, 100000+1):
    numerator = math.pow(-1, i+1)
    denomenator = 2 * i - 1
    k = numerator / denomenator
    sum += k
    if i == 10000 or i == 20000 or i == 30000 or i == 40000 or \
          i == 50000 or i == 60000 or i == 70000 or i == 80000 or \
          i == 90000 or i == 100000:
        print("PI is: ",format(4 * sum, ".3f"), "for i =", i)

endTime = time.time()
totalTime = (endTime - startTime)
print(format(totalTime, ".4f"), "seconds")
print("Sum is: ",format(4 * sum, ".3f"))