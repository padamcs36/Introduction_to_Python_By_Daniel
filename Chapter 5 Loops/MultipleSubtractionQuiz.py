import random
import time

correctCount = 0 #count the number of correct answers
count = 0 #control variable
NO_OF_QUESTIONS = 5 #constant, how many times our loop will executed
startTime = time.time()

while count < NO_OF_QUESTIONS:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    #if num1 is less than num2 then swap num2 with num1
    if num1 < num2:
        num1, num2 = num2, num1

    answer = int(input("What is "+str(num1)+" - "+str(num2)+" ?"))
    if num1 - num2 == answer:
        # print("You are correct")
        correctCount += 1
    # else:
    #     print("Your answer is wrong. Try again. What is "+str(num1)+" - "+str(num2)+" ?")
    #     print("Your answer is wrong", num1, "-",  num2, "=", num1 - num2)
    count += 1
endTime = time.time()
testTime = int(endTime - startTime)
print("Correct Questions is: ",correctCount, "out of ", NO_OF_QUESTIONS, "\nTest time is: ", testTime,"seconds")