import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# if number2 is greater than number1 then swap
if number1 < number2:
    number1, number2 = number2, number1
#predict the output of the quiz
answer = int(input("What is " +str(number1)+" - "+str(number2)+"?"))

while number1 - number2 != answer:
    answer = int(input("Wrong answer? Try again. What is "+str(number1)+" - "+str(number2)+"?"))
print("You got it.")