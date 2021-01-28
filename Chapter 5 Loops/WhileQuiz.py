import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

if num1 < num2:
    num1, num2 = num2, num1

answer = eval(input("What is "+str(num1)+" - "+str(num2)+" ? "))

while num1 - num2 != answer:
    answer   = eval(input("Wrong answer. Try again. What is "+str(num1)+" - "+str(num2)+" ? "))

print("You Got it.")

marks = eval(input("Enter your marks: "))

if marks >= 85 and marks <= 100:
    print("You Got A-1")
elif marks >= 75 and marks < 85:
    print("You Got A")
elif marks >= 65 and marks < 75:
    print("You Got B-1")
elif marks >= 60 and  marks < 65:
    print("You Got B")
elif marks >= 50 and marks < 60:
    print("You Got C")
else:
    print("Sorry You Fail.")


secretNum = random.randint(0, 99)

print("Enter guess number b/w 0 to 99")
guess = -1

while guess != secretNum:
    guess = eval(input("Enter your geuss: "))
    if guess == secretNum:
        print("Yes, the guess number is: ", secretNum)
    elif guess > secretNum:
        print("Your guess too high")
    elif guess < secretNum:
        print("Your guess too low.")