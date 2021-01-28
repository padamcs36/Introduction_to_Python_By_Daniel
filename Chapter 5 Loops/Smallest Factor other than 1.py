#Write a program to find the smallest factor other than one for the n
n = int(input("Enter number other than 1 (n>=2) ="))

factor = 2
while factor <= n:
    if n % factor == 0:
        break
    factor += 1
print("The smallest factor for ",n," is ", factor)