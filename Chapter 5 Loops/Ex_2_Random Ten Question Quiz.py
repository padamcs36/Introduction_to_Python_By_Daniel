import random
import time
correctCount = 0
NO_OF_QUESTION = 10
count = 0

startTime = time.time()
while count < NO_OF_QUESTION:
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 15)

    ans = eval(input(f"What is {num1} + {num2}?"))
    if ans == num1 + num2:
        correctCount += 1
        print(f"Correct, {num1}+{num2}={ans}")

    count += 1
endTime = time.time()
testTime = int(endTime - startTime)
print(f"Your correct answer is {correctCount} out of {NO_OF_QUESTION}\n"
      f"Total time you spend is {testTime} seconds")