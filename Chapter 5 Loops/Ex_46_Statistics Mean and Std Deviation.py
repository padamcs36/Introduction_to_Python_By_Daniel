#Compute mean and standard deviation of the besiness application
import math
sum = 0
sumSquare = 0
count = 0
print("Enter ten number : ")
for i in range(1, 10+1):
    x = eval(input())
    sum += x
    sumSquare += x * x
    count += 1

mean = sum / count
deviation = math.sqrt((sumSquare - ((math.pow(sum, 2)) / count)) / (count - 1))
print("Mean is ",format(mean, '.2f'))
print("The standard deviation is ", format(deviation, '.4f'))