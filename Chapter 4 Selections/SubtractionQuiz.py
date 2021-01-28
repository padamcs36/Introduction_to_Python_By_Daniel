import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

if num1 < num2:
    num1, num2 = num2, num1

answer = int(input("What is "+str(num1)+" - "+str(num2)+" ? "))

if num1 - num2 == answer:
    print("You are correct!")
else:
    print("You are wrong!")