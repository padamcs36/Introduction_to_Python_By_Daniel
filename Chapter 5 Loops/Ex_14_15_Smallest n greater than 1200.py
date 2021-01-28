#Find the smallest value of n^2 that is greater than the 12000
n = m = 1
while n * n <= 12000:
    n += 1
print(f"{n} is smallest square possible value that is greater than 12000. ")

while m * m * m <= 12000:
     m += 1
print(f"{m} is smallest cube possible value that is greater than 12000. ")

